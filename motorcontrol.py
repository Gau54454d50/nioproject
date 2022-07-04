#!/usr/bin/env python

# license removed for brevity
import rospy
from std_msgs.msg import String
    
def talker():
       pub = rospy.Publisher('MotorControl', String, queue_size=10)
       rospy.init_node('control', anonymous=True)
       rate = rospy.Rate(100) # 10hz
       while not rospy.is_shutdown():
           x=input("thruster number ")
           y=input("duty cycle for thruster"+str(x))
           hello_str = str(x)+" "+str(y)
           rospy.loginfo(hello_str)
           pub.publish(hello_str)
           rate.sleep()
   
if __name__ == '__main__':
    try:
       talker()
    except rospy.ROSInterruptException:
        pass
