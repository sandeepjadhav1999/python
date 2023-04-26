from app import add
import unittest
from unittest import result

class TestAddition(unittest.TestCase):
    def test_num_equals_to_ten(self):
        num1=10
        num2=10
        res=add(num1,num2)
        self.assertEqual(res,-1)

    def test_num_greater_than_ten(self):
        num1 = 11
        num2 = 30
        res = add(num1, num2)
        self.assertEqual(res, 41)
    def test_num_less_than_ten(self):
        num1 = 4
        num2 = 5
        res = add(num1, num2)
        self.assertEqual(res, -1)

    def test_result_greater_than_ten(self):
        num1 = 20
        num2 = 20
        res = add(num1, num2)
        self.assertGreater(res, 10)

    def test_result_lesss_than_ten(self):
        num1 = 2
        num2 = 3
        res = add(num1, num2)
        self.assertLess(res, 10)
        self.assertEqual(res, -1)

    def test_result_num1_num2_lesser(self):
        num1=11
        num2=12
        res=add(num1,num2)
        self.assertEqual(res,23)

    def test_result_num1_greater_num2(self):
        num1=12
        num2=11
        res=add(num1,num2)
        self.assertEqual(res,-1)

    def test_result_neg_not_allowed(self):
        num1=-1
        num2=-2
        res=add(num1,num2)
        self.assertLess(res,0)
if __name__=='__main__':
    unittest.main()
