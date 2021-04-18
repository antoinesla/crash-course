# prompts user for name and vote, tallies votes and number of responses
# TODO add check on user's vote input, and on repeat input
# TODO add check on user's name to see if someone voted twice


responses = {}

polling_active = True

while polling_active:
    name = input("name: ")
    response = input("yes/no: ")
    responses[name] = response
    repeat = input("repeat, yes/no: ")
    if repeat == "no":
        polling_active = False

yes_vote, no_vote = 0, 0

for key, value in responses.items():
    if value == "yes":
        yes_vote += 1
    if value == "no":
        no_vote += 1
    print(value)
    
print(f"number of votes: {len(responses)}, yes: {yes_vote}, no: {no_vote}")
