numbers = list(range(1,10))
newNumbers = []

for number in numbers:
    if number == 1:
        number = str(number) + "st"
    elif number == 2:
        number = str(number) + "nd"
    elif number == 3:
        number = str(number) + "rd"
    else:
        number = str(number) + "th"
    newNumbers.append(number)

print(numbers)
print(newNumbers)