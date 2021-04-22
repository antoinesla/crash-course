def count_word(filename, word):
    '''counts a rough approximate of a word in a given file'''
    try:
        with open(filename, encoding='utf8') as f:
            contents = f.read()
            print(type((contents)))
    except FileNotFoundError:
        print('file does not exist')
    contents = contents.lower()
    print(f'the word {word} appears {contents.count(word)} times in this book')

filename = r'text_files\frankenstein.txt'
word = input('which word would you like to count? ')
count_word(filename, word)
