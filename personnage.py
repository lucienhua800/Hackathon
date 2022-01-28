import pygame as pg 
game = True


class Personnage:
    def __init__(self,position,hp = 100,armor = 0,weapon = "basic knife",damage = 10):
        self.position = position
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.damage = damage
        
    
    def takeHit(self,extDamage):
        self.hp -= extDamage
        if (self.hp < 0):
            game = False
            print("Game Over")

    def attack(self, other, damage):
        other.takeHit(damage)

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.position[0] -= 1

        if keys[pg.K_RIGHT]:
            self.position[0] += 1
      
        if keys[pg.K_UP]:
            self.position[1] += 1
      
        if keys[pg.K_DOWN]:
            self.position[1] -= 1
    
    def changeRoom(self,door):
        self.position = [door[0], door[1]]
            
    
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






    
