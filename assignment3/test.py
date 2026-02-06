from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    def speak(self):
        print("meu meu meu")

class Cat:
    _count = 0  

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("meu meu meu")

    @classmethod
    def get_count(cls):
        return cls._count

class Dog:
    _count = 0  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog._count += 1 

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

    @classmethod
    def get_dog_count(cls):
        return cls._count

class BigDog(Dog): # inherits from Dog
    def __init__(self, name, age): 
        # Call the parent class's __init__ to set name/age
        super().__init__(name, age) 

    def fetch(self):
        print("Got it.")

    def speak(self):
        print("Woof Woof Woof") # overrides Dog.speak()

    def speak_verbose(self):
        # call Dog.speak(), then BigDog.speak()
        super().speak()
        self.speak()
"""
dog3 = BigDog("Butch", 3)
dog3.call_dog()
dog3.speak()
dog3.speak_verbose()

#dog34 = BigDog("Butch1", 3)
### Dog._count += 1 # illegal by convention
print(Dog.get_dog_count())
print("-----------------------")
print(dog3.__dict__)
#print("-----------------------")
#print(BigDog.__dict__)
"""

class Error(str):
   def __new__(cls, content):
      return str.__new__(cls, "ERROR: " + content.upper())

"""
x = Error("hello there")
print(x) # prints HELLO THERE
"""

"""
Decorators:
@classmethod - static class method decorator
@property
@dataclass
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius
"""
c = Circle(3)
print(c.area)    
print(c.diameter)
c.radius = 5
print(c.area)
print(c.diameter)


cat = Cat()
cat.speak()
cat.__dict__
"""

book1 = Book("Dune", "Frank Herbert")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Neuromancer", "William Gibson")

print(book1.__eq__(book2))

print(book1)
print(book1.__dict__)
print(book1.speak())
print(book2.title)          
print(book1 == book2) # True — same data, so considered equal
print(book1 == book3) # False — different data
