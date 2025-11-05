class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Tweet!")


animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.make_sound()
