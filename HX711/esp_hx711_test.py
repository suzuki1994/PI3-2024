from esp_hx711 import HX711
from time import *

hx711 = HX711(25, 26)   # DOUT= broche 25 (D3) et SCK = broche 26(D2)

hx711.tare()            # permet de ne pas prendre en compte le poids à vide
sleep_ms(2000)

hx711.set_scale(1955)   # permet d'afficher des grammes

while True:
    masse = hx711.get_units()
    print("masse =", masse)
    sleep_ms(1000)
