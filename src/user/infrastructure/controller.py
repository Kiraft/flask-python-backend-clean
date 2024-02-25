from .mongod import MongodUser
from ..application.response import UserResponse

class UserController:
    def __init__(self):
        self.mongo = MongodUser()
        self.response = UserResponse() 


    def validarUsuario(self, user, pasw):
        raw = self.mongo.userConnect(user, pasw)
        parsed = self.response.parsedUser(raw)

        return parsed