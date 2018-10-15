class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def paintCar(self, color):
        return "The {} - {}, has been painted {}.".format(self.make, self.model, color)


class Toyota(Car):

    def transmition(self, type_of_gear_box):

        if type_of_gear_box == "Auto":
            return "The {} - {}, is an automatic car.".format(self.make, self.model, type_of_gear_box)
       
        elif type_of_gear_box == "Manual":
        	return "The {} - {}, is a manual car.".format(self.make, self.model, type_of_gear_box)

        else:
        	return "Sorry. I am not aware of {} kind of transmition.".format(type_of_gear_box)


first_car = Car("Toyota", "U Wagon")
second_car = Toyota("Toyota", "Probox")

print(first_car.make, first_car.model)
print(first_car.paintCar("Red"))
print(second_car.transmition("Manual"))
