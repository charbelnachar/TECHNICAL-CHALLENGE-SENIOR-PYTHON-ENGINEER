import unittest


from src.exception.custom_exception import OutOfRange
from src.model.logic import DataCapture
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

    def test_add_repeat(self):
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        list_dic = data.get_list_dic()
        self.assertEqual(list_dic[numb]["repeat"],2)

    def test_add_len_dic(self):
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        self.assertEqual(data.get_len_dic(),2)

    def test_add_error(self):
        with self.assertRaises(OutOfRange):
            data = DataCapture()
            [data.add(numb) for numb in range(MAX_RANG+1)]

    def test_sorted_dic_to_list_type(self):
        data = DataCapture()
        data.add(2)
        data.add(1)
        data.add(3)
        dic = data.get_list_dic()
        self.assertIsInstance(dic,dict)
        data.sorted_dic_to_list()
        list_data = data.get_list_number()
        self.assertIsInstance(list_data,list)

    def test_sorted_dic_to_list_sort(self):
        data = DataCapture()
        aux_array = [1, 2, 3]
        data.add(2)
        data.add(1)
        data.add(3)
        data.sorted_dic_to_list()
        list_data = data.get_list_number()
        self.assertEqual(list_data, aux_array)

    def test_build_stats_return(self):
        data = DataCapture()
        return_data = data.build_stats()
        self.assertIsInstance(return_data,DataCapture)

    def test_less(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        capture.sorted_dic_to_list()
        capture.build_stats()
        less_value = capture.less(4)
        self.assertEqual(less_value,2)

    def test_greater(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        capture.sorted_dic_to_list()
        capture.build_stats()
        greater_value = capture.less(4)
        self.assertEqual(greater_value,2)

    def test_between(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        capture.sorted_dic_to_list()
        capture.build_stats()
        greater_value = capture.between(3,6)
        self.assertEqual(greater_value,4)



if __name__ == '__main__':
    unittest.main()
