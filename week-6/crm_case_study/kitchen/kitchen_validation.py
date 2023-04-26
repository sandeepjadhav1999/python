from kitchen.kiitechen_exception import *


def is_name_valid(name: str):
    if(name== None):
        raise InvalidNameException(
            'Please enter the valid Name'
        )
    return True

def is_location_valid(location: str):
    if (location == None):
        raise InvalidLocationException(
            'Please Enter the valid Location'
        )
    return True
    
def is_price_valid(price:int):
    if (price == 0):
        raise InvalidPriceException(
            'please Enter the valid price'
        )
    return True

def is_kitchen_valid(kitchen: dict):
    return is_name_valid(
        kitchen.get('name')
    )and is_price_valid(
        kitchen.get('price')
    )and is_location_valid(
        kitchen.get('location')
    )