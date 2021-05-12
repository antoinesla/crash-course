filename = r'text_files\programming_poll'

while True:
    message = input('why are you learning Python? (type "quit" to quit) ')
    if message == 'quit': break
    with open(filename, 'a') as f: f.write(f'{message}\n')

    