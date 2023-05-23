from flask_restx import Api

from application.controllers.home_controller import api as home_controller

api = Api(title='Top Movies API')

api.add_namespace(home_controller, path='/home')
