import unittest

from src.exception.custom_exception import NegativeNumber
from src.exception.custom_exception import OutOfRange
from src.model.logic import DataCapture
from src.model.logic import Stats
from src.utility.constante import MAX_RANG


class TestModelDataCapture(unittest.TestCase):
    def test_constructor(self):
        data = DataCapture()
        self.assertIsInstance(data,DataCapture)

        # self.assertEqual(True, False)  # add assertion here
    def test_default_value(self):
        data = DataCapture()
        self.assertEqual(data.get_list_dic(), {})
        self.assertEqual(data.get_list_number(), [])
        self.assertEqual(data.get_len_dic(), 0)

    def test_add(self):
        data = DataCapture()
        numb = 5
        data.add(numb)
        list_dic = data.get_list_dic()
        self.assertTrue(numb in list_dic)

    def test_add_error_raise(self):
        data = DataCapture()
        numb = "a"
        with self.assertRaises(ValueError):
            data.add(numb)
        numb = -1
        with self.assertRaises(NegativeNumber):
            data.add(numb)
        numb = MAX_RANG +5
        with self.assertRaises(OutOfRange):
            data.add(numb)



    def test_add_repeat(self):
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        list_dic = data.get_list_dic()
        self.assertEqual(list_dic[numb]["repeat"],1)

    def test_add_len_dic(self):
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        self.assertEqual(data.get_len_dic(),2)


    def test_build_stats_return(self):
        data = DataCapture()
        return_data = data.build_stats()
        self.assertIsInstance(return_data,Stats)

    def test_struct_dic(self):
        data = DataCapture()
        list_dict = data.get_list_dic()
        for numb in list_dict:
            self.assertIsInstance(list_dict[numb]["less"], int)
            self.assertIsInstance(list_dict[numb]["greater"], int)
            self.assertIsInstance(list_dict[numb]["greater"], int)



class TestModelStats(unittest.TestCase):

    def initial_data_test(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        return capture.build_stats()


    def test_less(self):
        stats = self.initial_data_test()
        less_value = stats.less(4)
        self.assertEqual(less_value, 2)

    def test_less_not_value_in_data_add(self):
        stats = self.initial_data_test()
        less_value = stats.less(5)
        self.assertEqual(less_value, 3)

    def test_greater(self):
        stats = self.initial_data_test()
        greater_value = stats.greater(4)
        self.assertEqual(greater_value, 2)

    def test_greater_not_in_data_add(self):
        stats = self.initial_data_test()
        greater_value = stats.greater(10)
        self.assertEqual(greater_value, 0)

    def test_between(self):
        stats = self.initial_data_test()
        greater_value = stats.between(3, 6)
        self.assertEqual(greater_value, 4)


if __name__ == '__main__':
    unittest.main()
