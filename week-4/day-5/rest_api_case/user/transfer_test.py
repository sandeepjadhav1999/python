from api import app

import unittest


class Withdraw(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_is_trans_valid(self):
        transfer= {
            'src_acc':19990001,
            'tar_acc':19990002,
            'amt':100
        }

        expected={
            'sts': 'success',
            'msg': 'amount transferred',
            'res': 1
        }
        response = self.client.post('/depo', json=transfer)
        actual = response.get_json()
        self.assertDictEqual(expected, actual)