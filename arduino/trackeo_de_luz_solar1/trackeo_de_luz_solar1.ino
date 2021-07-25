#include <Servo.h> 
// constantes
int servoPin = 8;
int fotoPin = A0;

// creacion de instancias de clase
Servo servo1;

// setup global
void setup(){
  servo1.attach(servoPin);
  Serial.begin(9600);
}

// ejecucion
void loop(){
  int max = 0;
  int finalDegrees = 0;
  for( int degrees=0 ; degrees<=120 ; degrees+=2){
  	servo1.write(degrees);
    int LDR = analogRead(fotoPin);
    if(LDR > max){
      max = LDR;
    	finalDegrees = degrees; 
    }
    delay(100);
  }
  Serial.print("La mejor inclinacion es de: ");
  Serial.println(finalDegrees);
  Serial.print("Pues alcanza un valor de: ");
  Serial.println(max);
  servo1.write(finalDegrees);
  delay(10000); //espera de 20 segundos
}
