from hx711 import HX711  # Importa a classe HX711 do módulo hx711

# Define os pinos de dados (DT) e o pino de clock serial (SCK) para o HX711
DATA_PIN = 2  # Pino conectado ao DT (Data)
SCK_PIN = 4   # Pino conectado ao SCK (Clock)

# Cria uma instância do objeto HX711
hx = HX711(DATA_PIN, SCK_PIN)
hx.set_scale(10)  # Define a escala do sensor
xvar = 0  # Inicializa a variável para armazenar o peso da tara conhecida

# Função principal
while True:
    hx.tare()  # Solicita a leitura do peso de tara conhecido
    read = hx.read()  # Lê os dados brutos do sensor
    average = hx.read_average()  # Lê a média do peso (com base em várias leituras)
    value = hx.make_average()  # Lê a média do peso de outra forma, utilizando uma divisão
    
    # Se o peso da tara ainda não foi armazenado
    if xvar == 0:
        xvar = value  # Armazena o peso da tara
    
    output = float(value) - float(xvar)  # Calcula o peso líquido subtraindo a tara

    # Exibe os valores lidos
    print('loop raw: ', read)  # Imprime o valor bruto da leitura
    print('loop x samples: ', average)  # Imprime a média de várias amostras
    print('kg: ', value, '->', output)  # Imprime o peso em quilogramas e o peso líquido calculado
    print('---------------')  # Imprime um separador para melhor visualização no loop


