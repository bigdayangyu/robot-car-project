# Gimbal On the Car Project 
### ROS based RC car with self-stalblized camera gimbal mounted
#### Check out the porject website <http://gimbalonthecar.weebly.com>

This RC car is armed with a stabilization platform for camera, to enhance the experience of comfortable and flexible video shooting, the camera gimbal is able to detect angle change of the gimbal, and adjust gimbal axis angle to make the camera staying horizontal to the ground. The car frame is made of carbon fiber such that it is lighter and more sustainable . Besides carbon fiber, aluminum are also available for future development . The camera car is modularized. None of parts is permanently fixed, so they are removable, interchangeable. We also design a 360 degree rotational robotic arm with four-bar mechanism to enable forward and backward motion, and provide extra degrees of freedom for camera shooting angle. 
<p align="center"><img src ="https://github.com/bigdayangyu/robot-car-project/blob/master/image/IMG_2432.JPG" width = 60% /></p>

Robot arm control and RC car control use ROS(Robotic Operating System) to provide communication between Linux based computer Raspberry pi and Arduino via ROS-arduino serial. The input signal is captured by a Python script, ROS publisher will publish the processed command to Arduino to control motor movement. User can use a Xbox Joystick controler to control robot arm, as well as the RC car movement. 

Gimbal mounted on this RC car is a camera stabilization system that uses motors to correct unwanted camera motion. Camera gimbal uses an independent arduino to control axis servos. Arduino takes accelerometer reading, and convert acceleration data into angle, then feed data back to PID controller to correct servo angle 
