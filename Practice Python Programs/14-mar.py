class User:
    def __init__(self, username, password, otp):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password
        print("Password update successfully.")

user1 = User("user1","1919sai","645482")

