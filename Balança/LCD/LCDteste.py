import machine  # Importa o módulo machine para controle de hardware
from machine import Pin, SoftI2C  # Importa classes e funções específicas do módulo machine
from lcd_api import LcdApi  # Importa a API LCD para controle do display LCD
from i2c_lcd import I2cLcd  # Importa o módulo I2C LCD para comunicação I2C com o LCD
from time import sleep  # Importa a função sleep do módulo time para pausas temporais

# Endereço I2C do LCD
I2C_ADDR = 0x27

# Número total de linhas e colunas do LCD
totalRows = 2  # Define que o LCD tem 2 linhas
totalColumns = 16  # Define que o LCD tem 16 colunas

# Inicializa o método I2C para o ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # Inicializa o método I2C para o ESP32, definindo os pinos SCL e SDA e a frequência

# Inicializa o objeto LCD
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)  # Cria uma instância do LCD, passando a comunicação I2C, endereço, e dimensões do display

# Loop contínuo para teste do LCD
while True:
    lcd.putstr("SUZUKI e ERIC")  # Exibe a string "SUZUKI e ERIC" no LCD
    sleep(2)  # Pausa por 2 segundos
    lcd.move_to(1, 1)  # Move o cursor para uma posição específica no LCD (coluna 1, linha 1)
    lcd.putstr("Lets Count 0-10")  # Exibe a string "Lets Count 0-10" no LCD
    sleep(2)  # Pausa por 2 segundos
    lcd.clear()  # Limpa o display LCD
    for i in range(11):  # Loop de 0 a 10
        lcd.putstr(str(i))  # Exibe o número atual no LCD
        sleep(1)  # Pausa por 1 segundo
        lcd.clear()  # Limpa o display LCD para exibir o próximo número
