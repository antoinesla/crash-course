class Dog:
    """attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} is now rolling over")


dog1 = Dog("waldo", 6)
dog2 = Dog("jeremy", 4)
print(f"first dog's name is {dog1.name}")
dog1.sit()
dog2.roll_over()

print(type(dog1))

# capitalized names refer to classes in python
# a funtiction that is part of a class is a method
# __init__() will be run automatically by the compiler when the class is
# created. its first parameter must be self, which will be passed automatically
# variables accessible with prefix self. are called attributes
