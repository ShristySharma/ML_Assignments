#include "Arduino.h"

void setup() { 
	Serial.begin(9600);
}

void loop() { 
	int sensorValue = analogRead(A0);
	double voltage = (3.3*sensorValue/666);
	Serial.println(voltage);
	delay(1000);
}
