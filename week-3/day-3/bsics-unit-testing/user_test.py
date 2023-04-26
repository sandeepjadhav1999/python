import unittest
from app_user import AppUser, InvalidUserNameException


class UserTest(unittest.TestCase):

    def test_check_user_non_null(self):
        dtc = dict()
        self.assertIsNotNone(dtc)

    def test_valid_user_name_length(self):
        user_name = 'Sbcdefghijklmn'
        password = '1333$#254'

        user = AppUser(user_name, password)
        self.assertEqual(user.user_name, 'Sbcdefghijklmn')
        self.assertEqual(user.password,'1333$#254')

    def test_invalid_user_name_length(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'abc'
            password = '1333#$254'

            AppUser(user_name, password)

    def test_user_name(self):
        with self.assertRaises(InvalidUserNameException):
            user_name='sandeep@jad'
            password='123#$45678'
            AppUser(user_name,password)

    def test_user_not_cap(self):
        with self.assertRaises(InvalidUserNameException):
            user_name='sandeepja'
            password='123#$4566'
            AppUser(user_name,password)

    def test_user_with_cap(self):
        user_name='Sandeepja'
        password='123456789'
        user= AppUser(user_name,password)
        self.assertEqual(user.user_name,'Sandeepja')
        self.assertEqual(user.password,'123456789')
    def test_password_special(self):
        user_name='Sandeepja'
        password='123456$#'
        user=AppUser(user_name,password)
        self.assertEqual(user.user_name,'Sandeepja')
        self.assertEqual(user.password,'123456$#')


if __name__ == '__main__':
    unittest.main()