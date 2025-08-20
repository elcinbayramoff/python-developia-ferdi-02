import random


# a = random.random()
# a = random.randint(1, 15)
# a = random.uniform(1.5,2.7)
# print(a)


# A = [1,2,3,4,5]

# # random.shuffle(A)
# # print(A)

# # random_num = random.choice(A)
# # print(random_num)
# random_nums = random.choices(A, k=2)
# print(random_nums)


"""
we will define a random number between 1 and 30
then we will ask user to enter a number to guess.
If it is more or less we will inform him/her
but if it correct then games is over
"""
a = random.randint(1, 50) # define random number
user1 = input("what is user1's name? ")
user2 = input("what is user2's name? ")

who_should_play = user1
while True:
    user_guess = int(input(f'{who_should_play} guess a number:')) 
    if user_guess > a:
        print('You are not correct, try less: ')
    elif user_guess < a:
        print('You are not correct, try more: ')
    else:
        print(f'{who_should_play} won the game!')
        break

    if who_should_play == user1:
        who_should_play = user2
    else:
        who_should_play = user1


