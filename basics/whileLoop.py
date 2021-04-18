# prompt = "please enter a pizza topping, or enter 'quit' to stop: "
# message = "" 
# flag = True

# while flag:
#     message = input(prompt)
#     if message == "quit": flag = False
#     else: print(f"adding {message} to your pizza")

# print("shutting down")


# 3 ways to test condition of while loop: flag (see above), condition in the 
# while loop, and break on condition

userList = []
userInput = ""
prompt = "insert value, 'print', 'erase' or 'quit': "

while userInput != "quit":
    userInput = input(prompt).strip()
    if userInput == "print":
        if userList:
            print("here are the values so far")
            for item in userList:
                print(item)
        else:
            print("no values in user list yet")
    elif userInput == "erase":
        print("erasing user list")
        userList = []
    else:
        userList.append(userInput)

print("shutting down")