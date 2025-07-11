from abc import ABC

class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("i can talk and walk")
class Dog(Animal):
    def move(self):
        print("i can bark")
a = Human()
a.move()
b = Dog()
b.move()

