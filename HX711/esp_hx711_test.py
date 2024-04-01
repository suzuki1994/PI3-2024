from hx711 import HX711  # Assuming you saved the class in hx711_custom.py


# Pin configuration
DATA_PIN = 2
SCK_PIN = 4

# Initialize the HX711 object
hx = HX711(DATA_PIN, SCK_PIN)

hx.set_scale(10)

xvar = 0
# Main function
while True:
    hx.tare()
    read=hx.read()
    average=hx.read_average()
    value=hx.make_average()
    
    if xvar==0:
        xvar=value
    
    output = float(value)-float(xvar)
    
    print('loop 5: ', read)
    print('loop 40: ', average)
    print('kg: ', value, '->', output)
    print('---------------')

