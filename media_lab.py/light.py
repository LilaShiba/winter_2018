import board
import neopixel
import weather

data = weather.url()
temp = weather.parse_call(data)
print(temp)

pixels = neopixel.NeoPixel(board.D18, 59)
