# class MyClass:
#     a = 5
#     def print_hello(self):
#         print("Hello, World!")

# b = MyClass()
# # print(b.a)
# # b.print_hello()
# b.secret_word = 'Secret'
# print(b.secret_word)


# class MyCar:
#     word = 'Car' # class variable
#     car_count = 0
#     def __init__(self, model, year):
#         self.model = model # instance(object) variable
#         self.year = year
#         MyCar.car_count += 1 

#     def detailed_info(self):
#         return f"{self.year} {self.model}"

# # car1 = MyCar("Toyota", 2020)
# # print(car1.detailed_info())

# # car2 = MyCar("Honda", 2021)
# # car2.model = "Honda Accord" 
# # print(car2.detailed_info())
# # print(car2.detailed_info())
# # print(car2.word)
# # print(MyCar.word)



# print(MyCar.car_count)

# car1 = MyCar("Toyota", 2020)
# print(car1.car_count)

# car2 = MyCar("Honda", 2021)
# print(car2.car_count)

# car3 = MyCar("Ford", 2022)
# print(car3.car_count)
# # 1. instance variables- 
# # 2. class variables
# # 3. object class variables


# class Person:
#     person_with_under_age = 0
#     person_with_more_age = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         if self.age < 18:
#             Person.person_with_under_age += 1
#         else:
#             Person.person_with_more_age += 1

#     @classmethod
#     def total_persons(cls):
#         return cls.person_with_under_age + cls.person_with_more_age
    
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
    
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
    
#     def __repr__(self):
#         return f"Person(name={self.name}, age={self.age})"

    
# person1 = Person("Alice", 16)
# # print(person1.__repr__())
# print(str(person1))
# person2 = Person("Bob", 20)
# person3 = Person("Charlie", 17) 
# print(f"Total persons under age: {Person.person_with_under_age}")
# print(f"Total persons 18 and over: {Person.person_with_more_age}")
# print(f"Total persons: {Person.total_persons()}")
# print(person1.is_adult(person1.age))  # False
# print(Person.is_adult(25))
