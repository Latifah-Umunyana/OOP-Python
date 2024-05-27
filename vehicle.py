class Vehicle:
    def __init__(self,model,make):
        self.model = model
        self.make = make

    def move(self):
        print("The vehicle is moving")


    def hoot(self):
        print("The bus is hooting")


class Bus(Vehicle):
    def __init__(self, model, make,capacity):
        super().__init__(model, make)
        self.capacity = capacity

    def check_capacity(self):
        print(f"The capacity is {self.capacity}")


class Lorry(Vehicle):
    def __init__(self, model, make,load_weight):
        super().__init__(model, make)
        self.load_weight = load_weight


    def unload(self):
        print("Unloading the lorry")


b = Bus("X","ISUZU",70)
b.move()
b.hoot()

l = Lorry("T","Mecedes",1000)
l.move()
l.unload()


class Animal:
    def __init__(self,name):

        self.name = name

    def move(self):
        pass

    def make_noise(self):
        pass


class Cat(Animal):
    def move(self):
        print("The cat is moving")

    def make_noise(self):
        print("meou")

class Bird(Animal):
    def move(self):
        print("The bird is flying")

    def make_noise(self):
        print("chirp")

class Fish(Animal):
    def move(self):
        print("The fish is moving")

    def make_noise(self):
        print("Boops")

        