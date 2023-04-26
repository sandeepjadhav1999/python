from flask_restful import Resource
from flask import request

from order.order_service import OrderService


class OrderListResource(Resource):

    def __init__(self, service: OrderService) -> None:
        self.service = service

    def get(self):

        return {
            'sts': 'success',
            'msg': 'all users in db',
            'res': self.service.list_all_order()
        }