class User():
    def __init__(self, user_id, user_name):
        self._user_id = user_id
        self._user_name = user_name
        self._access_l = 'user'

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_access_l(self):
        return self._access_l

    def set_name(self, name):
        self._user_name = name

class Admin(User):
    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь успешно добавлен в список")

    def remove_user(self, user_list,user):
        user_list.remove(user)

users = []
admin = Admin("n1", "Name1")
user1 = User("u1", "User1")

print (user1.get_user_name())
admin.add_user(users, user1)

