from flask import Flask
from flask_restful import Api

from customer.customer_routes import load_customer_routes
from crm_user.user_routes import load_user_routes
from kitchen.kitchen_routes import load_kitchen_routes
from menu.menu_route import load_menu_routes
from order.order_route import load_Order_routes
from promotion.promotion_route import load_promotion_routes

from database.connectivity import Connectivity

from flask_cors import CORS

connection = Connectivity().db

app = Flask(__name__)
CORS(app)

api = Api(app)

load_customer_routes(api, connection)
load_user_routes(api, connection)
load_kitchen_routes(api,connection)
load_menu_routes(api,connection)
load_Order_routes(api,connection)
load_promotion_routes(api,connection)


if __name__ == '__main__':
    app.run(debug=True)