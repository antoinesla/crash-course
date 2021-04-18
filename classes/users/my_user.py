from admin import Admin, Privilege

admin_privileges = [Privilege('kick', 'can kick user out of chat roo'), 
                    Privilege('ban', 'can ban user from all chat rooms'),
                    Privilege('invite', 'can invite user in a chat room')]
user1 = Admin('martin', 'dupont', admin_privileges)
user1.describe_user()
user1.describe_admin_privileges()