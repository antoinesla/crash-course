import json

filename = 'numbers.json'
try:
    with open(filename) as f:
        numbers = json.load(f)
except FileNotFoundError:
    print('file has not been generated')

print(numbers)