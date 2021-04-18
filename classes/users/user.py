class User:
    '''tutorial class to model user info on website'''

    def __init__(self, first_name, last_name):
        '''initializes user's attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.username = first_name + '.' + last_name
        self.login_attempts = 0

    def describe_user(self):
        message = f'{self.first_name}, {self.last_name}, {self.username}'
        print(message)

    def get_username(self):
        return self.username

    def get_login_attempts(self):
        return self.login_attempts

    def increment_login_attempts(self, login_attempts):
        self.login_attempts += login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0