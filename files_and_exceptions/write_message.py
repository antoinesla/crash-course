filename = r'text_files\programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('le zbi\n')


# Python can only write strings to a text file
# you have to convert numbers with .str() before writing them to the file