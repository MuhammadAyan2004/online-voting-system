import getpass

class User:
    users_db = {}
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False
    @classmethod
    def add_user(cls,username,password):
        if username in cls.users_db:
            print("username already exits. please try a different username.")
            return False
        cls.users_db[username]=cls(username,password)
        return True
    @classmethod
    def authenticate(cls, username, password):
        user = cls.users_db.get(username)
        if user and user.password == password:
            return user
        return None

def register_user():
        username = input("Enter a username.")
        password = input("enter a password.")

        if User.add_user(username, password):
            print("user registered successfully.")
        else:
            print("Registration failed.")
def login_user():
        username = input("Enter a username.")
        password = getpass.getpass("enter a password.")
        user = User.authenticate(username,password)
        if user:
            print("login successfully")
        else:
            print("invalid username or password")