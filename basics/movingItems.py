unconfirmed_users = ["alice", "bryan", "jean"]
confirmed_users = []

print(confirmed_users)

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verifying user {current_user}")
    confirmed_users.append(current_user)

print(confirmed_users)