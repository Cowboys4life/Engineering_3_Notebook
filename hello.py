# made by Nick

import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    print("Make it blue!")
    dot.fill((0, 0, 255))
    time.sleep(.5)
    print("Make it yellow")
    dot.fill((255,255,0))
    time.sleep(.5)
    dot.brightness = 0.2
