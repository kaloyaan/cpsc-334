#include <Stepper.h>
 
int in1Pin = 25;
int in2Pin = 33;
int in3Pin = 32;
int in4Pin = 35;
 
Stepper motor(64, in1Pin, in2Pin, in3Pin, in4Pin);  
 
void setup()
{
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
 
  // this line is for Leonardo's, it delays the serial interface
  // until the terminal window is opened
  //while (!Serial);
  
  Serial.begin(115200);
  motor.setSpeed(20);
}
 
void loop()
{
  if (Serial.available())
  {
    int steps = Serial.parseInt();
    motor.step(steps);
  }
}
