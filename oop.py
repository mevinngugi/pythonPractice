class Dog:

    # Class Attributes
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

    def description(self):
    	return "{} is {} years old.".format(self.name, self.age)

    def speak(self, sound):
    	return "{} say {}.".format(self.name, sound)


# Instantiate the Dog objext
maxi = Dog('maxi', 5)
rex = Dog('rex', 3)
tusker = Dog('tusker', 8)

print(maxi.name)
print(rex.age)

#print (a == b)

# print(type(a))

# Access the instance attributes
print("{} is {} and {} is {}.".format(maxi.name, maxi.age, rex.name, rex.age))

# Is Max a mammal?
if maxi.species == "mammal":
    print("{0} is a {1}!".format(maxi.name, maxi.species))

''' 
EXCERCISE: "The Oldest Dog"

Using the same Dog class, instantiate three new dogs, each with a different age.
Then write a function called, get_biggest_number(), that takes any number of
ages(*args) and returns the oldest one. Then output the age of the oldest
dog like so:

'''

# Determine the oldest dog


def get_biggest_number(*args):

    return max(args)


print("The oldest dog is {} years old.".format(
    get_biggest_number(maxi.age, rex.age, tusker.age)))


'''
INSTANCE METHOD

'''

mikey = Dog("Mikey", 6)

# Call our instance method
print(mikey.description())
print(mikey.speak("Gruff Gruff"))


'''
INHERITANCE
'''

class Bulldog(Dog):

	def movement(self, speed):
		return "Runs {}.".format(speed)

timmy = Bulldog("Timmy", 6)


print(timmy.movement("slow"))
