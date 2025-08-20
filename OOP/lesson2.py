# class Parent:
#     def greet(self):
#         return 'Hello, how are you?'
    

# class Child(Parent):
#     def greet_child(self):
#         return self.greet()

# child1 = Child()
# print(child1.greet())
# print(child1.greet_child())

#Create a Parent class Person with attributes of name surname and age
#Create a Child class Student that inherits from Person and adds an attribute of school_name


class A:
    pass

class B(A):
    pass

class C(A):
    pass
class D(B, C):
    pass

print(D.__mro__)  # Method Resolution Order
