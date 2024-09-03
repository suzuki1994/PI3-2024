from machine import Pin, SoftI2C  # Importa os módulos Pin e SoftI2C da biblioteca machine
from lcd_api import LcdApi  # Importa o módulo LcdApi da biblioteca lcd_api
from i2c_lcd import I2cLcd  # Importa o módulo I2cLcd da biblioteca i2c_lcd
from time import sleep  # Importa a função sleep da biblioteca time
from hx711 import HX711  # Importa a classe HX711 do módulo hx711

# Endereço I2C do LCD
I2C_ADDR = 0x27

# Número total de linhas e colunas do LCD
totalRows = 2  # Define que o LCD tem 2 linhas
totalColumns = 16  # Define que o LCD tem 16 colunas

# Inicializa o método I2C para o ESP32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)  # Define os pinos SCL e SDA para comunicação I2C e a frequência de operação

# Inicializa o objeto LCD
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)  # Cria uma instância do LCD, passando a comunicação I2C, endereço, e dimensões do display

# Define os pinos de dados (DT) e de clock serial (SCK) para o HX711
DATA_PIN = 2  # Pino conectado ao DT (Data)
SCK_PIN = 4   # Pino conectado ao SCK (Clock)

# Cria uma instância do objeto HX711
hx = HX711(DATA_PIN, SCK_PIN)  # Inicializa o HX711 com os pinos configurados
hx.set_scale(10)  # Define a escala para a leitura do sensor
xvar = 0  # Inicializa a variável para armazenar o peso de tara conhecido

# Loop contínuo para leitura do peso e exibição no display
while True:
    hx.tare()  # Solicita a leitura da tara conhecida
    value = hx.make_average()  # Lê o peso, calculando a média de várias amostras

    # Se o peso de tara ainda não foi armazenado
    if xvar == 0:
        xvar = value  # Armazena o valor da tara

    output = float(value) - float(xvar)  # Calcula o peso líquido subtraindo a tara
    print('kg: ', value, '->', output)  # Imprime o peso em quilogramas e o peso líquido calculado no console

    # Formata o texto a ser exibido no LCD
    linha_superior = "SUZUKI  ERIC"  # Texto fixo na linha superior
    linha_inferior = "Peso: %.2f g" % output  # Exibe o peso líquido na linha inferior com duas casas decimais

    # Limpa o LCD e escreve as linhas de texto
    lcd.clear()  # Limpa o display LCD
    lcd.putstr(linha_superior)  # Exibe o texto na linha superior
    lcd.move_to(0, 1)  # Move o cursor para o início da linha inferior
    lcd.putstr(linha_inferior)  # Exibe o peso na linha inferior

    sleep(1)  # Aguarda 1 segundo antes de realizar a próxima leitura e atualizar o display
