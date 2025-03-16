from abc import abstractmethod

class Swimable:
    @abstractmethod
    def swimming(self):
        pass

class Rideable:
    @abstractmethod
    def riding(self):
        pass

class Sea:
    def __init__(self):
        self.__creatures_in_the_sea = []
    
    def add_creatures_in_the_sea(self,_living_things):
        self.__creatures_in_the_sea.append(_living_things)
    
    def get_the_creatures(self):
        return self.__creatures_in_the_sea

class Fish(Swimable):
    def __init__(self,_colour,_size,_type):
        self.colour = _colour
        self.size = _size
        self.__is_alive = True
        self.fish_type = _type
    
    def set_status_die(self):
        self.__is_alive = False

    def get_status(self):
        return self.__is_alive

    def breathing(self):
        return "Blub blub"
    
    def __str__(self):
        return f"{self.fish_type}: Colour - {self.colour}, Size - {self.size}, Is Alive - {self.__is_alive}"
    
class Shark(Fish):
    def __init__(self,_colour,_size, _eatable_fish_size):
        super().__init__(_colour,_size,"Shark")
        self.eatable_fish_size = _eatable_fish_size
    
    def breathing(self):
        return "BLUB BLUB KAWK KAWK"

    def biting(self, fish):
        fish.set_status_die()
        return f"The shark has bite the fish"

class DaddyShark(Shark, Rideable):
    def __init__(self, _colour, _eatable_fish_size):
        super().__init__(_colour, "Large", _eatable_fish_size)
        self.hunting = []
        
    def working(self,_small_fish):
        self.hunting.append(_small_fish)

    def __str__(self):
        return f"Daddy Shark: Colour - {self.colour}, Size - {self.size}"

class MommyShark(Shark, Rideable):
    def __init__(self, _colour, _eatable_fish_size):
        super().__init__(_colour, "Large", _eatable_fish_size)
        self.__make_up = ["mascara", "lipstick"]

    def set_make_up (self,cosmetic):
        self.__make_up.append(cosmetic)

    def __str__(self):
        return f"Mommy Shark: Colour - {self.colour}, Size - {self.size}"

class BabyShark(Shark):
    def __init__(self, _colour, _eatable_fish_size):
        super().__init__(_colour, "Small", _eatable_fish_size)
        self._accessories = ["pacifier", "ribbon"]
    

    def biting(self, fish):
        if fish.size in ["Small","Medium"]:
            fish.set_status_die()
            return f"The shark can bite the fish"       
        else :
            return "Can't bite that one little boy, it's a little big for you!"


    def __str__(self):
        return f"Baby Shark: Colour - {self.colour}, Size - {self.size}"

class Fox:
    def piloting(self, ride:Rideable):
            return isinstance(ride, Rideable)
    
    def __str__(self):
        return f"Fox: Hurray"

def main() :
    sea = Sea()
    clownfish = Fish("Orange", "Small","Clownfish")
    dory = Fish("Blue", "Small","Dory")
    tuna = Fish("Grey", "Large","Tuna")
    red_snapper = Fish("Red", "Medium","Red_Snapper")

    baby_shark = BabyShark("Yellow", ["Small"])
    mommy_shark = MommyShark("Pink", ["Small", "Medium"])
    daddy_shark = DaddyShark("Blue", ["Small", "Medium", "Large"])

    fox = Fox()

    sea.add_creatures_in_the_sea(clownfish)
    sea.add_creatures_in_the_sea(dory)
    sea.add_creatures_in_the_sea(tuna)
    sea.add_creatures_in_the_sea(red_snapper)
    sea.add_creatures_in_the_sea(baby_shark)
    sea.add_creatures_in_the_sea(mommy_shark)
    sea.add_creatures_in_the_sea(daddy_shark)
    sea.add_creatures_in_the_sea(fox)

    fox.piloting(daddy_shark)
    daddy_shark.biting(clownfish)
    baby_shark.biting(tuna)

    for creature in sea.get_the_creatures():
        print(creature)
    

if __name__ == "__main__":
    main()