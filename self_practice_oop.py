class Person:

    # Class Attribute
    skin_color = "brown"

    def __init__(self, name, age, height):

        self.name = name
        self.age = age
        self.height = height

    # Instance Method
    # Basically used to change behavior of a class
    def movement(self, action):
        return "{} is {}.".format(self.name, action)


mevin = Person("Mevin", 26, 6)
peter = Person("Peter", 30, 5.8)
james = Person("James", 38, 5.2)
#print(Person("Mevin", 26, "6 feet"))

if mevin.skin_color == "chocolate":
    print("{} is {} years old and {} feet tall.".format(
        mevin.name, mevin.age, mevin.height), mevin.movement("walking"))
else:
    print("Looks like {} is of {} complexion, {} years old and {} feet tall.".format(
        mevin.name, mevin.skin_color, mevin.age, mevin.height), mevin.movement("running"))


'''
*ARGS

Find the oldes of the 3
'''


def the_oldest(*args):
    return max(mevin.age, peter.age, james.age)


print("The oldest guy in the crew is", the_oldest(), "years old")


'''
INHERITANCE
'''


class MyDaughter(Person):

    def talent(self, sing):

        return "{} sings {}.".format(self.name, sing)


mevins_daughter = MyDaughter("Ela", 2, 4)
print(mevins_daughter.talent("softly"))


print(mevins_daughter.talent("melodiously"),
      "but now,", mevins_daughter.movement("jogging"))
