print('give us two numbers and we will divide them')
print('type "q" to exit')

while True:
    first = input('first number: ')
    if first == 'q': break
    second = input('second number: ')
    if second == 'q': break

    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print("you can't divide by zero")
    except ValueError:
        print('you can only enter numbers')
    else:
        print(f'the answer is {answer}')