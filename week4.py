class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and identify as {self.gender}.")


person1 = Person(name="Okuhle" age=25, gender="Female")

person1.introduce()
