from ...mongo.connect import ConnectionMongo

class MongodUser:
    def __init__(self):
        self.connect = ConnectionMongo()

    def userConnect(self, user, pasw):
        db = self.connect.con
        col = db["usuarios"]

        col = col.find_one({"usuario": user, "password": pasw, "state": True}, {'_id': False, 'state': False, 'role': False})

        return col

