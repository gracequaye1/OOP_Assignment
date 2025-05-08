class Animal:
    def move(self):
        return "Moving in some way!"


class Dog(Animal):
    def move(self):
        return "Running on four legs! 🐕"

class Fish(Animal):
    def move(self):
        return "Swimming gracefully! 🐟"

class Bird(Animal):
    def move(self):
        return "Flying high in the sky! 🦅"

class Snake(Animal):
    def move(self):
        return "Slithering silently! 🐍"

# Using the classes
def animal_movement(animal):
    print(animal.move())

# Create instances of each animal
dog = Dog()
fish = Fish()
bird = Bird()
snake = Snake()

# Demonstrate polymorphism
animal_movement(dog)   # Output: Running on four legs! 🐕
animal_movement(fish)  # Output: Swimming gracefully! 🐟
animal_movement(bird)  # Output: Flying high in the sky! 🦅
animal_movement(snake) # Output: Slithering silently! 🐍