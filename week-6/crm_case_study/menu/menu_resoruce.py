from flask_restful import Resource
from flask import request
from menu.menu_service import MenuListService
from menu.menu_exception import *


class MenuResource(Resource):
    def __init__(self, service: MenuListService) -> None:
        super().__init__()
        self.service = service

    def get(self):
        return {
            'sts': 'success',
            'msg': 'all items in db',
            'res': self.service.list_all_menu()
        }

    def post(self):
        orderdetails = request.get_json()

        try:
            cnt = self.service.order_details(orderdetails)
            return {
                'sts': 'success',
                'msg': 'order placed successfully',
                'res': f'{cnt}'
            }, 201
        except InvalidNameException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Name'

            }, 400
        except InvalidQuntityException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Location'
            }, 400
        except InvalidTotalPriceException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Location'
            }, 400