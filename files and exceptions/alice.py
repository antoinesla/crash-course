def count_words(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'{filename} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'{filename} has approximately {num_words} words')

filename = 'frankenstein.txt'
count_words(filename)
filename = 'great_gatsby.txt'
count_words(filename)
filename = 'does_not_exist.txt'
count_words(filename)