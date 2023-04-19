#include "Arduino.h"
#include <math.h>


void setup() { 
  Serial.begin(9600);
}

void loop() { 
  int sensorValue = analogRead(A1); //resistance
  float voltage = ((3.3*sensorValue)/666);   //voltage divider rule
  float a = -0.0000029546268;
  float b = 0.0020663864;
  float c=  (2.5577569 - voltage);

 float Temp = abs(- b + sqrt((b*b - 4*a*c)/ 2*a)) ;
 //float test=sqrt(b*b - 4*a*c);
 Serial.println(sensorValue);
 Serial.println(voltage);
 Serial.println(Temp);
  //Serial.println();
  delay(1000);
}
