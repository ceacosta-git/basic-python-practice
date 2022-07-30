class Car:

    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

    def __str__(self):
        return "This car is a {color} {make} {model}".format(color=self.color,
                                                             make=self.make,
                                                             model=self.model)


if __name__ == "__main__":
    car = Car("grey", "Honda", "accord")
    print(car)
