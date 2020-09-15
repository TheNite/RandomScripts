import looker_sdk

looker = looker_sdk.init31("./looker.ini")
dict = {}

allow_admins = []

roles = {
    'Admin': [2],
    'Developer': [4],
    'User': [3],
    'Viewer': [5],
    'Lite Admin': [6],
}

def get_all_users():
    """Return a list of all users"""
    return looker.all_users()


for user in get_all_users():
    dict[user.id] = [user.email, user.role_ids]


def get_key(val: list):
    for key, value in roles.items():
        if len(val) > 1:
            return val
        elif val == value:
            return key


# for id, [email, role] in sorted(dict.items()):
#     if email not in allow_admins and not email.endswith('@looker.com'):
#         for role in looker.user_roles(id):
#             if role.name == 'Admin':
#                 #looker.set_user_roles(id, roles['Admin']) # update user role to only have admin
#

for id, [email, role] in sorted(dict.items()):
    if not email.endswith('@looker.com') and email not in allow_admins and role == roles['Lite Admin']:
        print(f'ID: {id}, Email: {email}, Role: {role}')
        #looker.set_user_roles(id, [])


