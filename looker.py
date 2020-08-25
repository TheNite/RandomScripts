import looker_sdk
import json
looker = looker_sdk.init31("./looker.ini")

def get_all_users():
    """Return a list of all users"""
    users = looker.all_users(fields="id, email")
    return users

users = get_all_users()

dict = {}
for user in users:
    print(f'Email:{user.email}, ID: {user.id}')
    dict[user.id] = user.email

print(sorted(dict.items()))