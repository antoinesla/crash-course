from random import choice

lottery_list = ['1', '2', '3', '4', '5', '6', '7', 
                '8', '9', 'a', 'b', 'c', 'd', 'e']

ticket_length = 5

my_ticket = []
for i in range(1,ticket_length + 1):
    my_ticket.append(choice(lottery_list))

attempts = 0

lottery_result = []

while lottery_result != my_ticket:
    lottery_result = []
    for i in range(1,ticket_length + 1):
        lottery_result.append(choice(lottery_list))
    print(lottery_result)
    attempts += 1

print(f'number of attempts: {attempts}')