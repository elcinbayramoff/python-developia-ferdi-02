# # def summing(a, b): # args
# #     return a + b


# # # def average(c, d): # args
# # #     return summing(c, d) / 2

# # # result = average(8, 4)
# # # print(result)

# # # def average(*args):

# # #     summing(*args)

# # # A = (1,2,3,4,5)
# # # summing(*A)

# #global

# def func_outer():
#     #enclosing
#     a = 7
#     def func_inner():
#         a = 9
#         b = 7
#         #local
#         print(a)

#     a = 8
#     func_inner()
#     print(a)

# a = 5
# func_outer()
# #local -> enclosing -> global -> built-in

# def symbol_count(string, symbol):
#     ...

# def uppercaser(values):
#     ...

# result = uppercaser(['salam','necesen','ali'])

#recursiveness

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))
