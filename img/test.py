from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

def cha_move(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)  
    delay(0.01)
    
z = -180
while(1):
    x = 400
    y = 90
    z = -180
    while (x <= 780):
        cha_move(x,y)
        x = x + 5

    while (y <= 550):
        cha_move(x, y)
        y = y + 5

    while (x >= 20):
        cha_move(x, y)
        x = x - 5

    while (y >= 90):
        cha_move(x, y)
        y = y - 5
    
    while (x <= 400):
        cha_move(x,y)
        x = x + 5

    while(z<=540):
        y = math.sin((z/360) * math.pi) * 200
        x = math.cos((z/360) * math.pi) * 200
        cha_move(400+x,290+y)
        z=z+3



    
close_canvas()
