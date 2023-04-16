import re


class UserModel:
    def __init__(self, id, fullname, email, login, password):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.login = login
        self.password = password

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @property
    def fullname(self):
        return self.__fullname

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @id.setter
    def id(self, value):
        self.__id = value

    @email.setter
    def email(self, value):

        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    @fullname.setter
    def fullname(self, value):
        self.__fullname = value

    @login.setter
    def login(self, value):
        self.__login = value

    @password.setter
    def password(self, value):
        self.__password = value

    def save(self):
        pass
