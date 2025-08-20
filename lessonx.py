A = {
    'name' : 'Elchin',
    'surname' : 'Bayramli',
}


# del A['name']
# print(A)
# print(A['age'])
# print(A.get('age', 18))
# print( list( A.keys() )  )

# for i in A.values():
#     print(i)

# for i in A.keys():
#     print(A.get(i))    

# for key, value in A.items():
#     print(key, value)

A = {
    'person1':{
        'name':'Elchin',
        'surname':'Bayramli'
    },
    'person2':{
        'name':'Ali',
        'surname':'Aliyev'
    }
}
# Print the name of first person in the dict A without using person1 as a key
# print(A['person1']['name'])

print('person2' in A)