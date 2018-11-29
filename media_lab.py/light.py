import board
import neopixel
import weather

data = weather.url()
temp = weather.parse_call(data)
print(temp)

pixels = neopixel.NeoPixel(board.D18, 59)

if temp > 50:
    pixels.fill((255,0,100))
else:
    pixels.fill((0,0,255))
