from flask_restful import Resource
from flask import request

from customer.customer_list_serive import CustomerListService



class CustomerListResource(Resource):

    def __init__(self, service: CustomerListService) -> None:
        self.service = service

    def get(self):

        return {
            'sts': 'success',
            'msg': 'all users in db',
            'res': self.service.list_all_users()
        }