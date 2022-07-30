from Car import Car


class UberCar(Car):
    def __init__(self, color, make, model, capacity, rate):
        super().__init__(color, make, model)
        self.capacity = capacity
        self.rate = rate

    def __str__(self):
        return ("""This Uber Car is a {} {} {}."""
                """ It can accommodate up to {} passengers and it costs ${} per mile.""")\
            .format(self.color, self.make, self.model, self.capacity, self.rate)


if __name__ == "__main__":
    non_uber = Car("green", "volkswagen", "jetta")
    uber = UberCar(non_uber.color, non_uber.make, non_uber.model, 3, 1.5)
    print(non_uber)
    print(uber)
