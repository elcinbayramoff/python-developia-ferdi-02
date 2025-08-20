# print(5 / 0) # ZeroDivisionError: division by zero
# a = int(input()) # ValueError: invalid literal for int() with base 10: 'salam'

# try:
#     a = int(input("Enter the first number: "))
#     b = int(input("Enter the second number: "))

#     print(a / b)

# # except ZeroDivisionError:
# #     print("Error: we can't divide by zero")
# # except ValueError:
# #     print("Error: Invalid input")
# # except (ZeroDivisionError, ValueError):
# #     print("Error: we can't divide by zero or invalid input")

# except Exception as e:
#     print("Caught an exception: ", e)
# # except:
# #     print("Caught an exception")
# else:
#     print("No exception was raised")
# finally:
#     print("This will always execute")



# c = int(input("Enter the first number: "))
# d = int(input("Enter the second number: "))

# print(c * d)

# raise Exception("This is an exception")

# raise ValueError("This is an exception")

# raise ZeroDivisionError("This is an exception")

# raise TypeError("This is an exception")

# raise NameError("This is an exception")


# print(5 / 0) #ZeroDivisionError



# Exception
# ZeroDivisionError 
# ValueError
# TypeError
# NameError
# IndexError
# KeyError
# AttributeError
# ImportError
# ModuleNotFoundError

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    print(a / b)
    print("No exception was raised")
except:
    5 / 0
finally:
    print("This will always execute")