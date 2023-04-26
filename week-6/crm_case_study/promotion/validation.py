import datetime
from promotion.promotion_exception import *
from datetime import date


def is_mobile_valid(promotion_id):
    if (len(promotion_id)<2):
        raise InvalidNameException(
            'please enter the valid ID'
        )
    return True

def is_quatity_valid(title):
    if (len(title)<5):
        raise InvalidNameException(
            'please enter the valid Title'
        )
    return True

def is_price_valid(text):
    if (len(text)<5):
        raise InvalidNameException(
            'please enter the valid amount'
        )
    return True

def is_promotion_valid(orderdetails: dict):
    return is_mobile_valid(
        orderdetails.get('promotion_id')
    ) and is_quatity_valid(
        orderdetails.get('title')
    )and is_price_valid(
        orderdetails.get('text')
    )