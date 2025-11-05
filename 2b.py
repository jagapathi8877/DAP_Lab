class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

    def fetch(self):
        print("The dog fetches the ball.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

    def scratch(self):
        print("The cat scratches the post.")

animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

dog = Dog()
dog.fetch()

cat = Cat()
cat.scratch()
