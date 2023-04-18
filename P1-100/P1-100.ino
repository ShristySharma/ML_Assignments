#include "Arduino.h"
#include <math.h>


void setup() { 
  Serial.begin(9600);
}

void loop() { 
  int sensorValue = analogRead(A1); //resistance
  float voltage = ((3.3*sensorValue)/((sensorValue+32)));   //voltage divider rule
 float a =0.0000249668363;
 float b =0.0154777438;
 float c= (310.40067 - voltage );
 float Temp = - b + sqrt((b*b - 4*a*c)/ 2*a) ;
 float test=sqrt(b*b - 4*a*c);
  Serial.println(sensorValue);
  Serial.println(voltage);
  Serial.println(Temp);
  Serial.println();
  delay(5000);
}
