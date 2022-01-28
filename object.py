class Object :
    def __init(self,name = "",value = 0):
        self.name = name
        self.value = value

class Gold(Object) :
    def __repr__(self):
        return f"{self.value} gold coins"

class Weapon(Object):
    def __repr__(self):
        return f"{self.name} with {self.value} ATT"

class Potion(Object):
    def __repr__(self):
        return f"health potion with {self.value} HP"

class Armor(Object):
    def __repr__(self):
        return f"{self.name} with {self.value} DEF"

class Helmet(Object):
    def __repr__(self):
        return f"{self.name} with {self.value} DEF"