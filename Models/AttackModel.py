import re


class AttackModel:
    def __init__(self, id, type, info):
        self.id= id
        self.type = type
        self.info = info


    @property
    def type(self):
        return self.__type

    @property
    def id(self):
        return self.__id

    @property
    def info(self):
        return self.__info


    @type.setter
    def type(self, value):
        self.__type = value


    @info.setter
    def info(self, value):
        self.__info = value


    def save(self):
        pass
