#include<Servo.h>

Servo servox, servoy;
char servo;
int angulo;
int valorx, valory;
void setup()
{
Serial.begin(9600);
servox.attach(2);
servoy.attach(3);
}
 
void loop()
{
  leer_dato();
  switch(servo){
    case 'x':
    valorx=angulo;
    break;
    case 'y':
    valory=angulo;
    break;
    default:
    valorx=0;
    valory=0;
    break;
    
    }

    servox.write(valorx);
    servoy.write(valory);
    delay(15);
 
}

void leer_dato(){
  if(Serial.available()>0){
    Serial.println(Serial.read());
    servo= Serial.read();
    angulo=Serial.parseInt();
    }
}
