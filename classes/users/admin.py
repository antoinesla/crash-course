from user import User

class Privilege:
    '''tutorial class to model privilege of an admin user'''

    def __init__(self, privilege, action):
        '''initializes attributes of a privilege'''
        self.privilege_name = privilege
        self.privilege_action = action
    
    def describe_privilege(self):
        '''describes what privilege is and what it allows'''
        print(f"'{self.privilege_name}'",
              f"privilege allows: '{self.privilege_action}'")


class Admin(User):
    '''tutorial class to model admin user'''

    def __init__(self, first_name, last_name, privileges):
        '''initializes admin's attributes'''
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def describe_admin_privileges(self):
        print('current admin user has following privileges:')
        for privilege in self.privileges:
            privilege.describe_privilege()