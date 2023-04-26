from flask_restful import Resource
from flask import request

from kitchen.kitchen_list_service import KitchenListService



class KitchenListResource(Resource):

    def __init__(self, service: KitchenListService) -> None:
        self.service = service

    def get(self):

        return {
            'sts': 'success',
            'msg': 'all users in db',
            'res': self.service.list_all_kitchen()
        }