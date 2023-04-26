from flask_restful import Resource
from flask import request
from promotion.promotion_service import PromotionListService
from promotion.promotion_exception import *


class PromotionResource(Resource):
    def __init__(self, service: PromotionListService) -> None:
        super().__init__()
        self.service = service

    def get(self):
        return {
            'sts': 'success',
            'msg': 'all items in db',
            'res': self.service.list_all_promotion()
        }

    def post(self):
        promotion = request.get_json()

        try:
            cnt = self.service.order_details(promotion)
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
        