import json

def get_stored_username():
    '''gets stored username, returns none if no stored value'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else: 
        return username

def get_new_username():
    '''prompts user for name and stores it in file, returns username'''
    filename = 'username.json'
    username = input('what is your name? ')
    with open(filename, 'w') as f:
            json.dump(username, f)
    return username

def greet_user():
    '''greets user with stored value, asks name if none stored'''
    username = get_stored_username()
    if username:
        print(f'welcome back {username}')
    else:
        username = get_new_username()
        print(f'welcome {username}')


greet_user()

# good practice: a value should either return the value you're expecting or 
# it should return None