from api import app

import unittest


class Withdraw(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_is_withdraw_valid(self):
        withdraw= {
            'acc_num_withdraw': 1999001,
            'amt':100
        }

        expected={
            'sts': 'success',
            'msg': 'amount deposited',
            'res': 1
        }
        response = self.client.post('/depo', json=withdraw)
        actual = response.get_json()
        self.assertDictEqual(expected, actual)