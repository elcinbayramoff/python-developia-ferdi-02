# A = [1,2,'Python',4,5,'Hello', 4.17, True, [1,2,3]]
# # A = '123'
# print(A)

# A = [10, 20, 30, 40, 50] # [50, 30, 10]
# print(A[-2])
# print(A[1:4])
# print(A[::-2])

# A = [1, 2, [1, 2, 3], 4]
# print(A[2][1])
# print([1, 2, 3][1])

# A = [1, 2, [1, [1,2,3], 3], 4]
# print(A[2][1][1])

# A = [10, 20, 30, 40, 50]

# # A[2] = 100
# A[1:3] = [100]
# A[1:3] = 'Hello'
# print(A)


A = [10, 20, 30, 40, 50]
B = [40, 50, 60, 70]
# A.insert(2,'Python')
# print(A)
# A.append('Python')
# print(A)

# C = A + B
# print(C)

# A.extend(B)
# print(A)

# A = [10, 20, 30, 40, 50]

# A.remove(30)
# A.pop(2)
# print(A)
# del A
# del A[2]

# print(A)


# A = [40, 20, 10, 30, 50]
# A.sort() # [10, 20, 30, 40, 50]
# A.sort(reverse=True) # [50, 40, 30, 20, 10]
# print(A)
# B = sorted(A)
# B = sorted(A, reverse=True)
# print(B)

# A = [8, 2, 1, 7, 6, 5, 4, 3]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 8, 7, 6, 5]



# A = [10, 20, 30, 40, 50]
# # B = A # It is not correct
# B = A.copy()
# A[2] = 100

# print(A,B)

# import copy

# A = [1, [1, 2, 3], 3]
# B = copy.deepcopy(A)

# A[1][1] = 100
# print(A)
# print(B)

A = [1, 2, 3, 4] # Palindrome