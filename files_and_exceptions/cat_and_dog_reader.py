def display_file_content(filename):
    '''displays content of file'''
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)

filename = r'text_files\catss.txt'
display_file_content(filename)

filename = r'text_files\cats.txt'
display_file_content(filename)
filename = r'text_files\dogs.txt'
display_file_content(filename)
