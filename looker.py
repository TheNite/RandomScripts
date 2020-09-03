import looker_sdk

looker = looker_sdk.init31("./looker.ini")
dict = {}

roles = {
    'Admin': [2],
    'Developer': [4],
    'User': [3],
    'Viewer': [5],
}

def get_all_users():
    """Return a list of all users"""
    return looker.all_users()


for user in get_all_users():
    dict[user.id] = [user.email, user.role_ids]

for id, email in sorted(dict.items()):
    print(f'ID: {id}, Email: {email}')
