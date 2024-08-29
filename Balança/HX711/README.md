# Pasta contendo relacionado ao HX711

O HX711 é um módulo conversor e amplificador de 24 bits que junto com uma célula de carga e um microcontrolador é possível montar uma balança digital. 

A célula de carga utilizada neste projeto é de uma 1KG, porém nada impede de substituir ela por uma de 3KG ou 5KG.
![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/C%C3%A9lula%20de%20carga.png)

O HX711 possui um lado que deve ser conectado com a célula de carga (E+ E- A- A+ B- B+), onde E+ (VCC fio vermelho) e E- (GND fio preto) e as saídas (A+ A-) e (B+ e B-), onde utilizamos as saídas A+ (fio verde) e A- (fio branco).
O outro lado onde tem os pinos (GND DT SCK VCC) são conectados com o microcontrolador (ESP32)
Neste projeto o pino 2 do ESP32 é o DT (data) e o pino 4 é o SCK (clock)
![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/HX711.jpg)
