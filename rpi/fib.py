import neopixel
import board
import time
# set up driver code
# The number of NeoPixels
num_pixels = 59
# init leds
pixel_pin = board.D18
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
                           pixel_order=ORDER)


def fib(n):
    if n <= 1:
        return n
    arr = [0 for x in range(n)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n):
        arr[i] = (arr[i -1] + arr[i - 2])
    return(arr[-1])

count = 0
light_range = 0
past_range = 0
while (light_range + past_range) < num_pixels:
    pixels.fill((255,255,255))
    count += 1
    past_range = light_range
    light_range = fib(count)
    p_count = 0
    while p_count < light_range:
        pixels[p_count] = (0,0,255)
        p_count += 1
    time.sleep(0.5)
