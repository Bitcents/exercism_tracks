from random import choice, randint

class Robot:
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _existing_names = set()

    def __init__(self):
        self.name = None
        self.name = self.set_name()
        
    
    def set_name(self) -> None:
        name = self.create_name()
        while name in Robot._existing_names:
            name = self.create_name()
        Robot._existing_names.add(name)
        return name

    def reset(self):
        previous_name = self.name
        self.name = self.set_name()
        Robot._existing_names.remove(previous_name)
        

    def create_name(self) -> str:
        return f"{choice(self.ALPHABETS)}{choice(self.ALPHABETS)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
    


