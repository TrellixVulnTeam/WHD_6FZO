#include <Wire.h> 

int medidor = 0;
int bandera = 0;
int umbral =  620;
int contador = 0;
double frecuencia = 0;

void setup(){
   Serial.begin(9600);
}

void loop(){

  for(int ciclos= 0; ciclos <100; ciclos++){
    medidor = analogRead(A1);
    // Conteo
    if (medidor > umbral)
    {
      bandera =1;
    }
    if (medidor < umbral && bandera ==1)
    {
      contador = contador+1;
      bandera=0;
    }
  }


  frecuencia = contador*6;
  //Serial.println(medidor);
  Serial.print("FREQ/MIN: ");
  Serial.println(frecuencia);
  delay(100);
  contador =0; 
}
