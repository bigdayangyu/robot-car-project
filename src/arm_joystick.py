#!/usr/bin/env python

import rospy
import curses
from sensor_msgs.msg import Joy

from std_msgs.msg import String, UInt16
from geometry_msgs.msg import Vector3 , Quaternion
def callback(data):
    joy_data = Quaternion()
    joy_data.x = 20*data.axes[6] # left positive
    joy_data.z = 20*data.axes[7] # up positive
    if data.buttons[2] == 1:
        joy_data.y = 120*data.buttons[2] #left positve 
    elif data.buttons[1] ==1:
        joy_data.y = 70*data.buttons[1] 
    if data.buttons[3] == 1:
        joy_data.w = 25600/6*data.buttons[3] #up positve 
    elif data.buttons[0] ==1:
        joy_data.w = -25600/6*data.buttons[0] 
    print(joy_data.x)
    pub.publish(joy_data)

def talker():
    global pub
    print('Please Enter command: s')
    
    pub = rospy.Publisher('servo_test', Quaternion, queue_size = 10)
    rospy.Subscriber("joy",Joy,callback)
    rospy.init_node('talker' , anonymous = True)
    rospy.Rate(10)
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
	
