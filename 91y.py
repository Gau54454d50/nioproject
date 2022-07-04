#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from smbus2 import SMBus			#import SMBus module of I2C
from time import sleep

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus =  SMBus(1) 	# or bus =  SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

def talker():
	pub = rospy.Publisher('gyroscope_accelerometer', String, queue_size=10)
	rospy.init_node('GyAc', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
        	#Read Accelerometer raw value
		acc_x = read_raw_data(ACCEL_XOUT_H)
		acc_y = read_raw_data(ACCEL_YOUT_H)
		acc_z = read_raw_data(ACCEL_ZOUT_H)
	
		#Read Gyroscope raw value
		gyro_x = read_raw_data(GYRO_XOUT_H)
		gyro_y = read_raw_data(GYRO_YOUT_H)
		gyro_z = read_raw_data(GYRO_ZOUT_H)
	
		#Full scale range +/- 250 degree/C as per sensitivity scale factor
		Ax = str(acc_x/16384.0)
		Ay = str(acc_y/16384.0)
		Az = str(acc_z/16384.0)
	
		Gx = str(gyro_x/131.0)
		Gy = str(gyro_y/131.0)
		Gz = str(gyro_z/131.0)
	

		x=str("Gx=" +Gx+u'\u00b0'+ "/s"+ "\tGy=" +Gy+ u'\u00b0'+ "/s"+ "\tGz=" +Gz+ u'\u00b0'+ "/s"+ "\tAx= " +Ax+"g"+ "\tAy=" +Ay+"g"+ "\tAz=" +Az+"g") 	
		sleep(1)
		rospy.loginfo(x)
		pub.publish(x)
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
