from api import app

import unittest


class Activate(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_is_activate_valid(self):
        activate= {
            'ac_sts':1,
            'acc_num':19990022
        }

        expected={
            'sts': 'success',
            'msg': 'account has been activated',
            'res': 1
        }
        response = self.client.post('/depo', json=activate)
        actual = response.get_json()
        self.assertDictEqual(expected, actual)