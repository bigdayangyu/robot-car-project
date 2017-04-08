#if defined(ARDUINO) && ARDUINO >=100
  #include "Arduino.h"
#else 
  #include <WProgram.h>
#endif
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/Float32.h>
#include <geometry_msgs/Vector3.h>
#include <Servo.h>

ros::NodeHandle  nh;
//std_msgs::UInt16 data_msg;
std_msgs::Float32 angle_msg;
//geometry_msgs::Vector3 motor_angle;

volatile unsigned long dt;
volatile unsigned long t0;
float angle;
// Servo parameters
Servo servo1;
Servo servo2;
void arm_actuator()
  {
    servo1.write(0);
    servo2.write(0);
    delay(100);
    }
void arm_move( const geometry_msgs::Vector3& cmd_msg)
{
  angle = 10;
  float servo_cmd1 = angle+cmd_msg.x;
  float servo_cmd2 = angle+cmd_msg.y;
  float servo_cmd3 = angle+cmd_msg.z;

  servo1.write(servo_cmd1);
  delay(10);
  servo2.write(servo_cmd2);
  delay(10);
  angle = servo_cmd1;
  angle_msg.data = angle;
  
  }

//ros::Subscriber<std_msgs::UInt16> sub("servo_test", &arm_move );
ros::Subscriber<geometry_msgs::Vector3> sub("servo_test", &arm_move );
ros::Publisher Actuator_msg("actuator_msg", &angle_msg);

void setup()
{
  servo1.attach(9);
  servo2.attach(10);
  arm_actuator();

  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(Actuator_msg);
  t0 = millis();
  delay(100);

}

void loop() 
{
  
  dt = millis() - t0;
  if (dt > 50)
  {
    Actuator_msg.publish(& angle_msg);
    delay(20);
    t0 = millis();
    nh.spinOnce();
    
   }
}
