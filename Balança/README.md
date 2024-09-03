# Arquivos relacionados com a balança 

Como hardware do projeto montou-se uma balança com os seguites componentes: um display de LCD 16x2 com o módulo I2C, uma célula de carga de 1KG, HX711 e o esp32. A balança pronta e funcionado encontra-se na figura abaixo.

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Balan%C3%A7a%20funcionando.png)

Podemos observar abaixo a estrutura da balança com a célula de carga

![](https://github.com/suzuki1994/PI3-2024/blob/main/Figuras/Balan%C3%A7a%20side%20view.jpeg)

![](https://www.toledobrasil.com/blob/upload/peso-padrao-2.gif)

A célula de carga é um transdutor resistivo que converte a força aplicada nela em um sinal elétrico. No GIF anterior, é mostrada a simulação do funcionamento da balança, onde uma força peso é aplicada, produzindo uma ligeira compressão na parte superior do sistema. Isso resulta em um sinal elétrico que é amplificado pelo módulo HX711. Esse sinal é então enviado para o microcontrolador (ESP32), que o converte em um valor numérico apresentado no display LCD. No nosso projeto, esse valor é enviado via Wi-Fi para serem utilizadas no algoritmo, onde posteriormente as calorias do alimento pesado são calculadas e armazenadas em um banco de dados.
