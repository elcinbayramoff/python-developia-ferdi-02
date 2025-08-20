# A = {1, 3, 4, 5, 5, 6, 6, 7, True + True, False}

# print(A)

# A = set([1, 2, 3, 4, 5])
# A = {4 ,3, 1 ,2}
# print(A)





# A = set('dog')
# print(A)

# A = {}
# A = set()
# print(type(A))

# A = {1, 2, 2, 3, 4}
# A.discard(2)
# print(A)
# A.remove(2)
# print(A)
# A.clear()
# del A
# print(A)

# A = {1, 2, 3}
# B = [3, 4, 5]
# C = A.union(B)
# print(C)
# A.update(B)
# print(A)
# C = A.intersection(B)
# print(C)
# C = A.difference(B)
# print(C)
# A.difference_update(B)
# print(A)

# C = A.symmetric_difference(B)
# print(C)

# A.symmetric_difference_update(B)
# print(A)
# C = A | B
# A |= B
# print(A.union(B))
# print(A | B)



# def sum_them(a, b):
#     print(a + b)
    

# sum_them(1, 5)

# sum_them(1 ,4)

# sum_them(1, 3)

# def func(a, b=4):
#     return a + b

# result = func(2)
# print(result)

# def func(name, surname, age):
#     return f"{name} {surname} - {age}"

# result = func('Elchin', surname='Bayramli', age="99")
# print(result)

# result = area_calc(2)
# print(result)


# def func(a, / ,b, * ,c, d):
#     print(a, b, c, d)

# func(1, b=2, d=3, c=4)

# def summing(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(a + b)

# summing(1, 2, 3, 4, 5, d=5, e=6)
# summing(1,2,3,4,5,6,7,8,9)

A= [1,2,3,4,5,6,7,8]
for i in A:
    if i % 2 == 0:
        print(i)