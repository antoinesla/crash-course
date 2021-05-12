def count_words(filename):
    try:
        with open(filename, 'r', encoding="utf8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'{filename} does not exist')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'{filename} has approximately {num_words} words')

filename = r'files_and_exceptions\text_files\frankenstein.txt'
count_words(filename)
filename = r'files_and_exceptions\text_files\great_gatsby.txt'
count_words(filename)
filename = r'files_and_exceptions\text_files\pride_and_prejudice.txt'
count_words(filename)
