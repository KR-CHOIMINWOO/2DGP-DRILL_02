from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_scene(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

def move_square():
    points = [(100, 100), (700, 100), (700, 500), (100, 500)]
    for i in range(4):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 4]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            draw_scene(x, y)
            delay(0.01)

def move_triangle():
    points = [(400, 500), (700, 100), (100, 100)]
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            draw_scene(x, y)
            delay(0.01)

def move_circle():
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 2):
        rad = math.radians(deg)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        draw_scene(x, y)
        delay(0.01)

while True:
    move_square()
    move_triangle()
    move_circle()

close_canvas()
character = load_image('character.png')