class User():
    def __init__(self, user_name, username, user_email, user_password ):
        self.user_name = user_name
        self.username = username
        self.user_email = user_email
        self.user_password = user_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__