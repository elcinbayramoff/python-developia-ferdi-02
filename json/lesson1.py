import json

# json_data = '{"name": "John", "age": 30, "city": "New York"}'
# python_data = json.loads(json_data)

# # print(python_data['name'])
# # print(python_data['age'])
# # print(python_data['city'])

# turned_json_data = json.dumps(python_data, indent=4,sort_keys=True, separators=(';','='))
# print(turned_json_data)

"""
w - write
x - creating
r - read
a - append

w+ - write, read
r+ - read, writing
"""

# with open('data.json', 'r') as f:
#     data = json.load(f)

# print(data)
data = {
    'breed': 'labrador',
    'color': 'brown',
    'age': 5,
    'name': 'Buddy'
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
    



