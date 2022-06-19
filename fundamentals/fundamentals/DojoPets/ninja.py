from pets import Pet
#the parent must have the child called into it.

class Ninja:
    all_ninjas = []
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    

    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self
    
    def let_sleep(self):
        self.pet.sleep()

#list of dictionaries for dog treats
treat_list = [
    {'dog' : "Dog Bones"},
    {'cat' : "Cat Treats"},
    {'lizard' : "Lizard Treats"},
    {'bird' : "Bird Treats"}
]

pet_food = [
    {'dog' : "Dog Food"},
    {'cat' : "Cat Food"},
    {'lizard' : "Lizard Food"},
    {'bird' : "Bird Food"}
]

ella = Pet("Ella", "dog", "Sit")
brian = Ninja("Brian", "Boyle", treat_list[0],pet_food[0], ella)
brian.bathe().let_sleep()



    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method
