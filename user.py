class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('My name is', self.name, 'and my email is', self.email)
