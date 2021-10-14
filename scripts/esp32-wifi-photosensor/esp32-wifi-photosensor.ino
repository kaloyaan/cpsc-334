/**
 * Interfacing Photoresistor using ESP32
 * By TechMartian
 *
 */
//cosntants for the pins where sensors are plugged into.
const int sensorPin = 35;
//Set up some global variables for the light level an initial value.
int lightInit;  // initial value
int lightVal;   // light reading

void setup()
{
  Serial.begin(115200);
  lightInit = analogRead(sensorPin);
  Serial.println("Just read:");
  Serial.println(lightInit);
  //we will take a single reading from the light sensor and store it in the lightCal        //variable. This will give us a prelinary value to compare against in the loop
}

void loop()
{
  lightVal = analogRead(sensorPin); // read the current light levels
  Serial.println(lightVal);
  delay(10);
}
