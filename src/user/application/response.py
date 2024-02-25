class UserResponse():

    @staticmethod
    def parsedUser(raw):
        if raw is not None:
           
            return raw
        else:
            raise Exception("Usuario no válido")