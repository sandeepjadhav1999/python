import datetime
from customer.customer_exceptions import *


def is_mobile_valid(mobile: str) -> bool:
    if(len(mobile) != 10):
        raise InvalidCustomerMobileException(
            'Mobile Length Should equals to 10'
        )
    return True


def is_name_valid(name: str):
    if(len(name) < 8):
        raise InvalidCustomerNameException(
            'Name should be min 8 character long'
        )
    return True


def is_email_valid(email: str):
    if ('@' not in email):
        raise InvalidCustomerEmailException(
            'Please enter the Valid Email ID'
        )
    return True
def is_dob_valid(dob: datetime):
    if (dob == None):
        raise InvalidCustomerDOBException(
            'Please Enter the valid date of birth'
        )
    return True
def is_location_valid(location: str):
    if (location == None):
        raise InvalidCustomerLocException(
            'Please Enter the valid Location'
        )
    return True

def is_status_vald(status: str):
    if (status not in [1,0]):
        raise InvalidCustomerStatusException(
            'please the proper status'
        )
    return True


def is_customer_valid(customer: dict):
    return is_mobile_valid(
        customer.get('mobile')
    ) and is_name_valid(
        customer.get('name')
    ) and is_email_valid(
        customer.get('email')
    ) and is_dob_valid(
        customer.get('dob')
    )and is_location_valid(
        customer.get('location')
    ) and is_status_vald(
        customer.get('status')
    )