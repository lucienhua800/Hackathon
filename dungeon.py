import pygame as pg
from random import randint
import numpy as np
from personnage import * 
from object import * 
W, H = 20, 20
X, Y = 30, 30

# définition de la gridarray:
tiret=[1,1,1,1,1,1,1,1,1,1,1,1,0,0]
salle1=tiret*10

WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
colors = np.array([[0,0,0], [255,255,255]])
gridarray = np.array([[1]*600,[0]*600,[0]*600,[0]*600,[1]*600]).transpose()
surface = pg.surfarray.make_surface(colors[salle1])
# surface = pg.surfarray.make_surface(np.array([]))


pg.init()
screen = pg.display.set_mode((X*W, Y*H))
clock = pg.time.Clock()

image = pg.image.load("shovel.png").convert_alpha()
 

def draw_background():  
    screen.fill(BLACK)
    screen.blit(image, (0, 50))
    screen.blit(surface, (0, 5))
    pg.display.flip()


def draw_tile(x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, color, rect)

running = True
while running:

    clock.tick(4)
    draw_background()
    pg.display.update()

pg.quit()
