from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from hx711 import HX711

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     # Inicializando o método I2C para ESP32

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Define os pinos DT e SCK
DATA_PIN = 2  # Pino conectado ao DT
SCK_PIN = 4  # Pino conectado ao SCK

# Cria uma instância do objeto HX711
hx = HX711(DATA_PIN, SCK_PIN)
hx.set_scale(10)
# Solicita a tara conhecida
xvar = 0
while True:
    hx.tare()
    read=hx.read()
    average=hx.read_average()
    value=hx.make_average()
    
    if xvar==0:
        xvar=value
    
    output = float(value)-float(xvar)
    
    print('loop 5: ', read)
    print('loop 20: ', average)
    print('kg: ', value, '->', output)
    print('---------------')
    # Formata o texto para exibir no LCD
    linha_superior = "SUZUKI  ERIC"
    linha_inferior = "Peso: %.2f g" % output

    # Limpa o LCD e escreve as linhas
    lcd.clear()
    lcd.putstr(linha_superior)
    lcd.move_to(0, 1)
    lcd.putstr(linha_inferior)

    # Aguarda um pouco antes da próxima leitura e atualização do LCD
    sleep(1)




