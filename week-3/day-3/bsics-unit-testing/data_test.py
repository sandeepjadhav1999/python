from data_sts import DataManipulation
import unittest
import datetime

class DataStrTest(unittest.TestCase):
    def setUp(self):
        self.dm=DataManipulation()
    
    def test_is_list(self):
        lst=self.dm.list_of_elements(True,False,True)
        self.assertIsInstance(lst,list)
    
    def test_check_invalid_types(self):
        lst=self.dm.list_of_elements(datetime.date(2021,2,20),45,'abc')
        self.assertIsNone(lst)
        #self.assertEqual(lst,12)
    def test_check_valid_type(self):
        lst=self.dm.list_of_elements('abc',45,45.6,True)
        self.assertIsNotNone(lst)
    def test_check_it_is_tuple(self):
        lst=self.dm.square_each_tuple(1,1,1,1)
        self.assertIsInstance(lst,tuple)
    def test_valid_square(self):
        lst=self.dm.square_each_tuple(1,2,3,4)
        expected=(1,4,9,16)
        self.assertTupleEqual(lst,expected)
    def test_add_tuple(self):
        lst=self.dm.add_new_element_tuple(1,2,3,lt=4)
        expected=(1,2,3,4)
        self.assertTupleEqual(lst,expected)
    def Test_sort_dict_(self):
        lst=self.dm.sort_dec_dict({1:2,2:3,3:4})
        expected=()
    def teardown(self):
        self.dm=None

if __name__=='__main__':
    unittest.main()
