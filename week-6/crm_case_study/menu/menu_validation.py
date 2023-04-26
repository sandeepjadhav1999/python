import datetime
from menu.menu_exception import *
from datetime import date


def is_mobile_valid(customer_id_mobile):
    if (len(customer_id_mobile)!=10):
        raise InvalidNameException(
            'please enter the valid mobile number'
        )
    return True

def is_quatity_valid(total_quantities):
    if (total_quantities <0):
        raise InvalidQuntityException(
            'please enter the valid quatity'
        )
    return True

def is_price_valid(total_price):
    if (total_price<0):
        raise InvalidTotalPriceException(
            'please enter the valid amount'
        )
    return True

def is_menu_valid(orderdetails: dict):
    return is_mobile_valid(
        orderdetails.get('customer_id_mobile')
    ) and is_quatity_valid(
        orderdetails.get('total_quantities')
    )and is_price_valid(
        orderdetails.get('total_price')
    )