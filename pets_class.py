class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # ear method
    def eat(self):
        self.is_hungry = False
        #return self.is_hungry

# Child class (inherits from Dog class)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))


if dog.is_hungry == True:
    print("My dogs are hungry")
    

elif dog.is_hungry == False:
    print("My dogs are not hungry")
    print(dog.name)
    print(Bulldog.is_hungry)

for dog in my_pets.dogs:
    if dog.is_hungry = False:
        print("My dogs are not hungry")

#def isDogHungry(args):
#    if 



    

'''
#################################################
        MY WORKING
#################################################

# Pets class

class Pet(Dog):

    def myPet(self):
        return "{} is {}.".format(self.name, self.age)


tom = Pet("Tom", 6)
fletcher = Pet("Fletcher", 7)
larry = Pet("Larry", 9)

if Dog.species == "mammal":
    print(tom.myPet())
    print(fletcher.myPet())
    print(larry.myPet())
    print("And they're all mammals, of course.")'''
