from flask import Flask, request
from flask_restful import Api, Resource

from user.user_resource import UserResource
from user.deposite_amount import deposite
from user.withdraw_amount import Withdraw
from user.transfer_amount import Transfer
from user.display_account import Display
from user.activate import Activate
from db.connectivity import Connectivity
from flask_cors import CORS


app = Flask(__name__)

CORS(app)
api = Api(app)
connection = Connectivity().db 

 # for maintaining single db connection

api.add_resource(
    UserResource,  # shape of user resource
    '/user',
    resource_class_kwargs={'db': connection}  # imp step
)
api.add_resource(
    deposite,  # shape of user resource
    '/depo',
    resource_class_kwargs={'db': connection}  # imp step
)

api.add_resource(
    Withdraw,  # shape of user resource
    '/withdraw',
    resource_class_kwargs={'db': connection}  # imp step
)

api.add_resource(
    Transfer,  # shape of user resource
    '/trans',
    resource_class_kwargs={'db': connection}  # imp step
)


api.add_resource(
    Display,  # shape of user resource
    '/display',
    resource_class_kwargs={'db': connection}  # imp step
)

api.add_resource(
    Activate,  # shape of user resource
    '/activate',
    resource_class_kwargs={'db': connection}  # imp step
)



if __name__ == '__main__':
    app.run(debug=True)