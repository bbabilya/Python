
class Pet:
    list_of_pets = []
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.hp = 20
        self.energy = 15
        Pet.list_of_pets.append(self)
        # self.owner = ninja()

    def sleep(self):
        self.energy += 25
        print(f"{self.name} has {self.energy} now!")
        return self

    def eat(self):
        self.energy += 5
        self.hp += 10
        return self

    def play(self):
        self.hp += 5
        return self

    def noise(self):
        if self.type == "dog":
            print("Woof")
        else:
            print("Meow")






    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
