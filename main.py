import pyb
from ws2812 import Neopixel

LEDS = [[None for _ in range(60)] for i in range(3)]

for i in range(60):
    LEDS[0][i] = (0xff, 0x00, 0xff)
    if i % 2:
        LEDS[1][i] = (0xff, 0x00, 0x00)
        LEDS[2][i] = (0x00, 0x00, 0xff)
    else:
        LEDS[1][i] = (0x00, 0x00, 0xff)
        LEDS[2][i] = (0xff, 0x00, 0x00)
index = 0
neo = Neopixel(led_count = 60)
neo.intensity = 0.5
neo.update_leds(LEDS[index])
pot = pyb.ADC(pyb.Pin.board.X19)
pb  = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)
prev_pot = pot.read()

while True:
    if abs(prev_pot - pot.read()) > 10:
        prev_pot = pot.read()
        pot.intensity = min(prev_pot / 2900.0, 1)
        neo.update_leds(LEDS[index])
    if pb.value() == 1:
        index = (index + 1) % len(LEDS)
        neo.update_leds(LEDS[index])
        