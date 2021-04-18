filename = r'text_files\guest_book.txt'
message = ''


while True:
    message = input('please enter your name ("quit" to quit): ')
    if message == 'quit': break
    with open(filename, 'a') as f: f.write(f'{message}\n')

print('shutting down')