
class User:
    users = [{
        "user_id": 1,
        "username": "Ayub",
        "role": "Admin",
        "email": "ayub@gmail.com",
        "password": "ayub"

    }]

    def create(self, username, role, email, password):
        new_user = {"user_id": len(User.users) + 1,
                    "username": username,
                    "role": role,
                    "email":email,
                    "password":password
                    }
        User.users.append(new_user)  # save user

    """ get all users """
    def get_all_users(self):
        return User.users

    """ get single user """
    def get_one_users(self, user_id):
        for one_user in User.users:
            if one_user['user_id'] == "user_id":
                return one_user

            return False
