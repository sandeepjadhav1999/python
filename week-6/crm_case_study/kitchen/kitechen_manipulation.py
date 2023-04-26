from flask_restful import Resource
from flask import request
from kitchen.kitchen_service import KitchenService
from kitchen.kiitechen_exception import *


class KitchenManipulationResource(Resource):
    def __init__(self, service: KitchenService) -> None:
        super().__init__()
        self.service = service

    def post(self):
        kitchen = request.get_json()

        try:
            cnt = self.service.save_kitchen(kitchen)
            return {
                'sts': 'success',
                'msg': 'kitchen saved successfully',
                'res': f'{cnt}'
            }, 201
        except InvalidNameException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Name'

            }, 400
        except InvalidLocationException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Location'
            }, 400