from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_char_square():
    x = 0
    y = 90
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
def move_char_circle():
    cx = 400
    cy = 300
    r = 200
    for i in range(0, 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = cx + r * math.cos(math.radians(i))
        y = cy + r * math.sin(math.radians(i))
        character.draw_now(x, y)
        delay(0.01)

while(True):
    move_char_square()
    move_char_circle()

close_canvas()
