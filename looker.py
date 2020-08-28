import looker_sdk

looker = looker_sdk.init31("./looker.ini")
dict = {}


def get_all_users():
    """Return a list of all users"""
    return looker.all_users(fields="id, email, ")


for user in get_all_users():
    dict[user.id] = user.email

for id, email in sorted(dict.items()):
    if email.endswith("@looker.com"):
        print(f'ID: {id}, Email: {email}')
