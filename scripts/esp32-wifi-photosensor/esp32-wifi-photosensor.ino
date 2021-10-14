
#include <WiFi.h>

const char* ssid     = "yale wireless";
const char* password = "";

const uint16_t port = 8090;
const char * host = "172.29.32.254";

//constants for the pins where sensors are plugged into.
const int sensorPin = 35;
//Set up some global variables for the light level an initial value.
int lightVal;   // light reading

WiFiClient client;

void setup()
{
  Serial.begin(115200);

  delay(10);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

}

void loop()
{
  lightVal = analogRead(sensorPin); // read the current light levels
//  Serial.println(lightVal);
//  delay(100);

  if (!client.connect(host, port)) {
   
     Serial.println("Connection to host failed");
   
     delay(1000);
     return;
  }
  
  Serial.println("Connected to server successful!");
 
  client.print(String(lightVal));
  Serial.println(String(lightVal));

//  Serial.println("Disconnecting...");
//  client.stop();
  
  delay(10000);
}
