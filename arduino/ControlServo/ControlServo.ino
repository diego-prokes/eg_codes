// Incluye la libreria con las funciones para controlar el servo
#include <Servo.h> 
// Creamos una variable que almacena qué pin controlará al servo.
int servoPin = 3; 
// Crea un objeto del tipo servo
Servo Servo1; 
void setup() { 
   // Hacemos que el servo sea controlado por el pin antes declarado
   Servo1.attach(servoPin); 
}
void loop(){ 
   Servo1.write(0); 
   delay(1000); 
   // 90 grados
   Servo1.write(90); 
   delay(1000); 
   // 180 grados
   Servo1.write(180); 
   delay(1000); 
}