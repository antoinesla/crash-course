while True:
    first = input('input a number to be added (type "q" to quit): ')
    if first == 'q': break
    second = input('input the second number (type "q" to quit): ')
    if second == 'q': break

    try:
        result = int(first) + int(second)
    except ValueError:
        print('you can only enter numbers')
    else: 
        print(f'the result is {result}')

print('shutting down')