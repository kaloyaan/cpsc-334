/* CPSC334 ESP->Python

    Associated documents: 

    Python:
    stem-player.py
*/

const int joy_x = 0;
const int joy_y = 4;
const int but = 19;
const int swch = 1;

int joy_x_val = 0;
int joy_y_val = 0;
int but_val = 0;
int swch_val = 0;

void setup() {
  Serial.begin(115200);

  pinMode(joy_x, INPUT);
  pinMode(joy_y, INPUT);
  pinMode(but, INPUT);
  pinMode(swch_val, INPUT);
}

void loop() {

  int vals[] = {joy_x_val, joy_y_val, but_val, swch_val};

  joy_x_val = analogRead(joy_x); // read analog pin 35
  joy_y_val = analogRead(joy_y); // read analog pin 34
  but_val = digitalRead(but);
  swch_val = digitalRead(swch);

  Serial.print("[");
  Serial.print(vals[0]); // send pin reading via serial
  Serial.print(",");
  Serial.print(vals[1]); // send pin reading via serial
  Serial.print(",");
  Serial.print(vals[2]); // send pin reading via serial
  Serial.print(",");
  Serial.print(vals[3]); // send pin reading via serial
  Serial.println("]");

  delay(50);

}
