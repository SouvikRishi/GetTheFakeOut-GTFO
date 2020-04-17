import json

list1 = [{'id': 123, 'data': 'qwerty', 'indices': [1,10]}, {'id': 345, 'data': 'mnbvc', 'indices': [2,11]}]
x=json.dumps(list1)
print(type(x))