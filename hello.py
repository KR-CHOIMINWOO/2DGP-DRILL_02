from pico2d import *

open_canvas()

img = load_image('character.png')
for x in range(0, 9):
    for y in range(0,7):
        img.draw_now(x * 100, y * 100)
delay(2)

close_canvas()


