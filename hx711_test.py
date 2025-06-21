
'''
GND Yellow
DT orange
SCK red
VCC brown
'''




    #!/usr/bin/python3
from hx711 import HX711

try:
    hx711 = HX711(
        dout_pin=3,
        pd_sck_pin=2,
        channel='A',
        gain=64
    
    )

    hx711.reset()   # Before we start, reset the HX711 (optional)
    
    measures = hx711.get_raw_data(times=3)
finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

print("\n".join(measures))