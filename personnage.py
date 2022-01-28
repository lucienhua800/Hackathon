import pygame as pg 
game = True
keys = pg.key.get_pressed()

class Personnage:
    def __init__(self,position = [0,0],hp = 100,armor = 0,weapon = "basic knife",damage = 10):
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.damage = damage
        
    
    def takeHit(self,extDamage):
        self.hp -= extDamage
        if (self.hp < 0):
            game = False
            print("Game Over")

    def attack(damage):
        pass

    def move(self):
        if keys[pg.K_LEFT]:
            self.position[0] -= 1

        if keys[pg.K_RIGHT]:
            self.position[0] += 1
      
        if keys[pg.K_UP]:
            self.position[1] += 1
      
        if keys[pg.K_DOWN]:
            self.position[1] -= 1
            
    
class Player(Personnage): 
    def __init__(self,position = [0,0],hp = 100,armor = 0,weapon = "basic knife",damage = 10, mana = 200, inventory = [], gold = 0):
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.damage = damage
        self.mana = mana 
        self.inventory = inventory
        self.gold = gold

    # def openInventory(self):
    #     #Montre l'inventaire 
    #     #TODO
    # def useObject(self):
    #     #TODO






    
