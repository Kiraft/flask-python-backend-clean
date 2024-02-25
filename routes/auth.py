from flask import Blueprint, request
from decouple import config
from validators.validators import parsedRespond, hasErrorMsg, checkArgs
from src.user.infrastructure.controller import UserController

auth = Blueprint(name='auth', import_name= __name__)

@auth.route('%s%s/%s' % (config('API_PATH'), config('API_VERSION'),  'user/login'), methods=["GET"])
def validar_usuario():

    try:
        # bearer_token = inspectCred(request.headers)
        checkArgs(['usuario','password'], request.args)

        _userCL = UserController()
        data = _userCL.validarUsuario(request.args['usuario'], request.args['password'])
        return parsedRespond(data)

    except Exception as err:
        return hasErrorMsg(err)