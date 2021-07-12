void setup(){
	pinMode(13, OUTPUT);
}

void loop(){
	digitalWrite(13, HIGH);	//voltaje alto
	delay(5000);			//delay de 1 seg.
	digitalWrite(13, LOW);	//voltaje bajo
	delay(1000);			//delay de 1 seg.
}