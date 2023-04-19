#include "Arduino.h"
#include <math.h>
#include<LiquidCrystal.h>
LiquidCrystal lcd (12,11,5,4,3,2);

void setup() { 
  Serial.begin(9600);
  lcd.begin(16,2);
}

void loop() { 
  int sensorValue = analogRead(A0); //resistance
  double voltage = ((3.3*sensorValue)/666);   //voltage divider rule
  double a = -0.0000029546268;
  double b = 0.0020663864;
  double c=  (2.5577569 - voltage);

 double Temp = (- b + sqrt((b*b - 4*a*c)))/ (2*a) ;
 Serial.println(sensorValue);
 Serial.println(voltage);
 Serial.println(Temp);
  lcd.print("Temp(in Celcius)");
  lcd.setCursor(1,2);
  lcd.print(Temp);
  delay(1000);
  lcd.clear();
}
