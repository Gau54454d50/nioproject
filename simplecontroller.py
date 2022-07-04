#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import pigpio
#pwm frequency
pwm_frequency= 15000
#pwm gpio pins
pwm1 = 12
pwm2 = 13
pwm3 = 18
pwm4 = 19
#dir gpio pins
dir1 = 5
dir2 = 6
dir3 = 23
dir4 = 24
pi = pigpio.pi()


def callback(data):
    print (data.data.split())
    if (data.data[0] =='1') :
        pi.hardware_PWM(pwm1, pwm_frequency, int(data.data.split()[1])*10000)
    elif (data.data[0] =='2') :
        pi.hardware_PWM(pwm2, pwm_frequency, int(data.data.split()[1])*10000)   
    elif (data.data[0] =='3') :
        pi.hardware_PWM(pwm3, pwm_frequency, int(data.data.split()[1])*10000) 
    elif (data.data[0] =='4') :
        pi.hardware_PWM(pwm4, pwm_frequency, int(data.data.split()[1])*10000)

    rospy.loginfo(rospy.get_caller_id() + 'Thruster'+data.data[0]+'value='+data.data.split()[1])

def listener():

    rospy.init_node('thrust_control', anonymous=True)
    rospy.Subscriber('MotorControl', String, callback)
    


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
