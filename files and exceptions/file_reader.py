file_path = r'text_files\pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input('enter your birthday, in the format ddmmyyyy: ')

if birthday in pi_string:
    print('your birthday appears in the first million digits of pi')
else: 
    print('sowwy :(')