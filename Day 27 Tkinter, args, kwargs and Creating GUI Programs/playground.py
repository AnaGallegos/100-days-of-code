def add(*arg):
    return sum(arg)

print(add(2,3,5)) 

def calculate(n, **kwargs):
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")
        self.colour = kw.get("colour")

my_car = Car(make = "Nissan")
print(my_car.make)
