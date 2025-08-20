# class PersonA:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def greet(self):
#         return f'Hello From PersonA, my name is {self.name} {self.surname} and I am {self.age} years old.'

# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def greet(self):
#         return f'Hello, my name is {self.name} {self.surname} and I am {self.age} years old.'
    
# class Student(PersonA, Person):
#     def __init__(self, name, surname, age, school_name):
#         # Person.__init__(self, name, surname, age)
#         super().__init__(name, surname, age)
#         self.school_name = school_name

#     @property
#     def full_name(self):
#         return f'{self.name} {self.surname}'


#     def greet_student(self):
#         result = super().greet() + f' I study at {self.school_name}.'
#         return result

# student1 = Student('John', 'Doe', 20, 'XYZ High School')
# # print(student1.greet_student())
# # print(student1.greet_student())  
# print(student1.full_name)



# class Lion:
#     def __init__(self):
#         self.name = "Lion"

#     def sound(self):
#         return "Roar!"
    
# class Cat:
#     def __init__(self):
#         self.name = "Cat"

#     def sound(self):
#         return "Meow!"

# class Dog:
#     def __init__(self):
#         self.name = "Dog"

#     def sound(self):
#         return "Woof!"
    
# class Rabbit:
#     def __init__(self):
#         self.name = "Rabbit"

#     def sound(self):
#         return "Hop!"
    
# lion1 = Lion()
# cat1 = Cat()
# dog1 = Dog()
# rabbit1 = Rabbit()

# animals = [lion1, cat1, dog1, rabbit1]
# for animal in animals:
#     print(animal.name)


#Encapsulation in Python classes
# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, amount):
#         if amount < 0:
#             print("Invalid amount. Balance must be positive.")
#             return
#         else:
#             self.__balance = amount

# bank_account = Bank(1000)
# # print(bank_account.__balance)  X
# # print(bank_account._Bank__balance)
# bank_account.set_balance(1500)
# print(bank_account.get_balance()) 

class Animal:
    ...

class Cat(Animal):
    # self.breed = 'cat'
    self.bre

class Dog(Animal):
    ...

class Toy:
    ...
toy1 = Toy()

class PetShop:
    ...
    """
    pets
    toys
    self.toys = []
    self.pets = []
    add_pet(    )
    remove_pet()
    add_toy(toy)
    remove_toy()

    own_a_pet(breed='cat')
    buy_a_toy(name='car')
    """