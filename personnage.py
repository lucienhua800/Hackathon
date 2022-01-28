from re import A
import pygame as pg 


class Personnage:
    def __init__(self,position,hp = 100,armor = 0,weapon = "basic knife",damage = 10, alive = True):
        self.position = position
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.damage = damage    
    def takeHit(self,extDamage):
        diff = (extDamage - self.armor)
        if diff > 0 : 
            self.hp -= diff
        if (self.hp < 0):
            alive = False
    def attack(self, other):
        other.takeHit(self.damage)
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
    def openInventory(self):
        for i in range(len(self.inventory)):
            print(f"Object n°{i} : Type = {self.inventory[i][0]}, Value = {self.inventory[i][1]}"  )
        print("use an object by writing its number, or press another key to close inventory")
        inp = int(input)
        if inp < len(self.inventory):
            if self.inventory[inp][0] == "Weapon" : 
                self.damage = self.inventory[inp][1]
            elif self.inventory[inp][0] == "Potion" : 
                self.hp += self.inventory[inp][1]
            elif self.inventory[inp][0] == "Armor" : 
                self.armor = self.inventory[inp][1]

class Monstre(Personnage):
    def __init__(self,name,position,hp = 100,armor = 0,weapon = "basic knife",damage = 10, alive = True):
        self.position = position
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.damage = damage
        self.alive = True

def combatPhase(p,o):
    fight = True
    while fight : 
        clock = pg.time.Clock()
        clock.tick(10)
        keys = pg.key.get_pressed()
        if keys[pg.K_x]:
            p.attack(o)
        o.attack(p)
        if (not o.alive()):
            fight = False
        elif (not p.alive()) :
            game = False
            print("Game over !")
            
    
    



    
