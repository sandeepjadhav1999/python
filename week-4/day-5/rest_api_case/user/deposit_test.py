import sys
# Add the ptdraft folder path to the sys.path list
# sys.path.append('/api')
print(sys.path)

import app

import unittest
from unittest import result

class deposites(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_is_depo_valid(self):
        deposites= {
            'acc_num_deposit':19990001,
            'amt':1000
        }

        expected={
            'sts': 'success',
            'msg': 'amount deposited',
            'res': 1
        }
        response = self.client.post('/depo', json=deposites)
        actual = response.get_json()
        self.assertDictEqual(expected, actual)


    # def test_is_depo_acc_invalid(self):
    #     deposite={
    #         'acc_num_deposite':19990020,
    #         'amt':-100
    #     }
    #     expected={
    #         "sts": "fail",
    #         "msg": "please enter the proper amount"
    #     }
        
    #     response = self.client.post('/depo', json=deposite)
    #     actual = response.get_json()
    #     self.assertDictEqual(expected, actual)


    def tearDown(self) -> None:
        pass


if __name__=='__main__':
    unittest.main()








