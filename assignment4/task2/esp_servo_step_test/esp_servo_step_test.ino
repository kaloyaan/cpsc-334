#include <ESP32Servo.h>
#include <Stepper.h>
 
int in1Pin = 25;
int in2Pin = 33;
int in3Pin = 32;
int in4Pin = 35;

const int stepsPerRevolution = 512; //4096
 
Stepper myStepper(64, in1Pin, in2Pin, in3Pin, in4Pin);  //64

Servo myservo;  // create servo object to control a servo
// 16 servo objects can be created on the ESP32

int pos = 0;    // variable to store the servo position
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
int servoPin = 13;

void hitBell(){
    for (pos = 0; pos <= 20; pos += 2) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);    // tell servo to go to position in variable 'pos'
      delay(15);             // waits 15ms for the servo to reach the position
    }
    for (pos = 20; pos >= 0; pos -= 2) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);    // tell servo to go to position in variable 'pos'
      delay(15);             // waits 15ms for the servo to reach the position
    }
}

void setup() {
  // Allow allocation of all timers
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  myservo.setPeriodHertz(50);    // standard 50 hz servo
  myservo.attach(servoPin, 500, 2400); // attaches the servo on pin 18 to the servo object
  // using default min/max of 1000us and 2000us
  // different servos may require different min/max settings
  // for an accurate 0 to 180 sweep
  myservo.write(0);


  // set the speed at 400 rpm:
  myStepper.setSpeed(500);
  // initialize the serial port:
  Serial.begin(9600);

  hitBell();
  hitBell();
  hitBell();
  myStepper.step(4096);
}

int loc = 0;

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time LED was updated

// constants won't change:
const long interval = 10000;           // interval at which to blink (milliseconds) 

void loop() {
    unsigned long currentMillis = millis();
  
  hitBell();
  
  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    for (pos = 0; pos <= 20; pos += 2) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);    // tell servo to go to position in variable 'pos'
      delay(15);             // waits 15ms for the servo to reach the position
    }
    delay(10);
    for (pos = 20; pos >= 0; pos -= 2) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);    // tell servo to go to position in variable 'pos'
      delay(15);             // waits 15ms for the servo to reach the position
    }
  }
    // if the LED is off turn it on and vice-versa:
    myStepper.step(stepsPerRevolution);
}
