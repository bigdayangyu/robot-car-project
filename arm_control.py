#!/usr/bin/env python

import rospy
import curses

from std_msgs.msg import String, UInt16
from geometry_msgs.msg import Vector3

def talker():
    rospy.init_node('talker' , anonymous = True)
    pub = rospy.Publisher('servo_test', Vector3, queue_size = 10)

    rospy.Rate(10);

    while not rospy.is_shutdown():
        arm_actuator = Vector3()
        screen = curses.initscr()
        print('Please Enter command: s')
        
        try:
            curses.noecho()
            curses.curs_set(0)
            screen.keypad(1)
            event = screen.getch()
            
            if event == curses.KEY_LEFT:
                arm_actuator.x = 100
            elif event == curses.KEY_RIGHT:
                arm_actuator.y = 100
            elif event == curses.KEY_UP:
                arm_actuator.x = 20
            else:
                arm_actuator.x = 90
        finally:
            curses.endwin()

    
        pub.publish(arm_actuator)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
	
