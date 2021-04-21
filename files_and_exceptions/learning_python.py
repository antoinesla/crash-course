
# reading the file line by line while stripping each line
with open(r'text_files\learning.txt') as f:
    string_list = [line.rstrip() for line in f]

new_string_list = []

for line in string_list: 
    new_string_list.append(line.replace('Python', 'C++'))

for line in string_list: 
    print(line)

for line in new_string_list: 
    print(line)


# # reading the whole file in one go
# with open(r'text_files\learning.txt') as f:
#     whole_file = f.read()

# print(type(whole_file))
# print(whole_file)


# # reading all the lines at once and saving them in a list
# with open(r'text_files\learning.txt') as f:
#     line_list = f.readlines()

# print(type(line_list))
# for line in line_list:
#     print(line.strip())