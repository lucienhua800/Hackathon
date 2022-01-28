from turtle import update
import pygame as pg
import numpy as np
from personnage import * 
from object import * 
import random
from random import Random as rnd

object_list = []

global game
game = True
class room:
    def __init__(self, number_monster, number_objects, lx,ly,trapdoors):
        self.number_monster = number_monster
        self.number_objects = number_objects
        self.lx = lx
        self.ly = ly
        self.trapdoors = trapdoors

        grille = [['.']*(ly+2) for k in range((lx+2))]
        # définir les bords
        for j in range(self.ly+2):
            grille[0][j] = '-'
            grille[self.lx+1][j] = '-'
        for i in range(1,self.lx+1):
            grille[i][0] = '|'
            grille[i][self.ly+1] = '|'
        # definition of monsters
        for k in range(number_monster):
            res  = False
            while res ==False:
                a = random.randint(1,lx+1)
                b = random.randint(1,ly+1)
                if grille[a][b] == '.':
                    res = True
            grille[a][b] = 'M'
        # definitions of objects
        #li_objects = ['*','j','&','A']
        for k in range(number_objects):
            res  = False
            while res ==False:
                a = random.randint(1,lx+1)
                b = random.randint(1,ly+1)
                if grille[a][b] == '.':
                    grille[a][b] = 'O'
                    res = True
            #obj = rnd.choice(li_objects)
            # grille[a][b] = obj
        
        self.grille = grille


def generation_map(number_rooms, strandard_size):
    carte = np.array([[';'] * (number_rooms * strandard_size * 2) for i in range(number_rooms * strandard_size * 2) ])
    liste_trapdoors = []
    liste_rooms = []
    for k in range(number_rooms):
        lx = random.randint(strandard_size//2, strandard_size)
        ly = random.randint(strandard_size//2, strandard_size)
        pos_trapdoors = []
        if k==0:
            pos_trapdoors.append([number_rooms * strandard_size * 2 - strandard_size //4 -ly, strandard_size //2])
        if k==(number_rooms-1):
            pos_trapdoors.append([3*strandard_size //4, strandard_size //2])
        else:
            pos_trapdoors.append([ (k+1) * strandard_size * 2 - strandard_size //4, strandard_size //2])
            pos_trapdoors.append([ (k+1) * strandard_size * 2 - strandard_size //4 -ly, strandard_size //2])
        
        liste_trapdoors += pos_trapdoors
        
        roomk = room(k, k, lx,ly,pos_trapdoors)

        #Position initiale du chevalier
        if k ==0:
            res = False
            while res ==False:
                a = random.randint(1,lx+1)
                b = random.randint(1,ly+1)
                if roomk.grille[a][b] == '.':
                    res = True
                    roomk.grille[a][b] = 'P'

        liste_rooms.append(roomk)
        p,q = np.array(roomk.grille).shape()
        carte[ (number_rooms-k) * strandard_size * 2 - strandard_size //4 - ly (number_rooms-k) * strandard_size * 2- strandard_size //4][ strandard_size //4 : strandard_size //4 + ly ] = np.array(roomk.grille)
        return [carte, liste_trapdoors, liste_rooms]

salletest=room(5,0,0,30,30)


W, H = 20,20
X, Y = 30,30

# définition de la gridarray:
tiret=[1,1,1,1,1,1,1,1,0,0]
salle1=[tiret*30,tiret*30,[0,0,0,0,0,0,0,0,0,0]*30,[0,0,0,0,0,0,0,0,0,0]*30,tiret*30,tiret*30]




WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
colors = np.array([[0,0,0], [255,255,255]])
gridarray = np.array([[1]*600,[0]*600,[0]*600,[0]*600,[1]*600]).transpose()
# surface = pg.surfarray.make_surface(colors[np.array(salletest.grille).transpose()])

pg.init()
screen = pg.display.set_mode((X*W, Y*H))
clock = pg.time.Clock()
mur=pg.image.load("murt.png").convert_alpha()
image = pg.image.load("shovel.png").convert_alpha()
 

def draw_background():  
    y=10
    screen.fill(BLACK)
    for ligne in salletest.grille:
        x=10
        for element in ligne:
            if element=='-' or '|':
                screen.blit(mur, (x,y))
                x+=5
        y+=5

    screen.blit(image, (0, 50))
    # screen.blit(surface, (0, 5))
    pg.display.flip()


def draw_tile(x, y, color):
    """
    x and y in tiles coordinates
    translate into pixel coordinates for painting
    """
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, color, rect)
player = Personnage([0,0])

def update_position(pos,keys):
    if keys[pg.K_LEFT]:
        pos[0]+=1
    if keys[pg.K_RIGHT]:
        pos[1]+=1
    if keys[pg.K_UP]:
        pos[0]-=1
    if keys[pg.K_DOWN]:
        pos[1]-=1
    if keys[pg.K_a]:
        Player.openInventory()
    return pos

sleep = False
while game :
    clock.tick(10)
    keys = pg.key.get_pressed()
    next_pos = update_position(player.position,keys)
    if carte[next_pos] == '.':
        player.position = next_pos
    elif carte[next_pos] == "-":
        pass #ne rien faire
    elif carte[next_pos] == "O" :
        otype = rnd.randint(1,4)
        if otype == 1 : #or
            player.gold += rnd.randint(10,100)
        elif otype == 2: #potion
            player.inventory.append(["Potion",rnd.randint(10,50)])
        elif otype == 3: #armor
            player.inventory.append(["Armor",rnd.randint(5,10)])
        elif otype == 4: #weapon
            player.inventory.append(["Weapon",rnd.randint(20,30)])
    elif carte[next_pos] == "m":
        monster = Monstre("Goblin",next_pos,hp = rnd.randint(50,80))
        combatPhase(player,monster)

    draw_background()
    pg.display.update()

pg.quit()