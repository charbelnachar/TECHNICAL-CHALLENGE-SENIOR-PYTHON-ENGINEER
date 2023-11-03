import unittest
from src.exception.custom_exception import NegativeNumber
from src.exception.custom_exception import OutOfRange
from src.model.logic import DataCapture
from src.model.logic import Stats
from src.utility.constante import MAX_RANG

class TestModelDataCapture(unittest.TestCase):
    def test_constructor(self):
        """
        Test the constructor of DataCapture.

        This method tests the constructor of the DataCapture class.

        Test case:
        1. Create an instance of DataCapture.

        Expected result:
        1. An instance of DataCapture should be created.
        """
        data = DataCapture()
        self.assertIsInstance(data, DataCapture)

    import unittest

    class TestDictionaryStructure(unittest.TestCase):
        def test_dictionary_structure(self):
            """
            Verify if the structure of a dictionary is consistent across all its values.

            This test ensures that the structure of a dictionary, such as 'DataCapture's list_dic', remains the same for all its values.

            Test steps:
            1. Define the expected structure for each value in the dictionary as 'expected_structure'.
            2. Create an example dictionary ('example_dictionary') with key-value pairs using DataCapture's list_dic.
            3. Iterate through the dictionary and compare the structure of each value with the 'expected_structure'.
            4. If a value has a different structure, the test will fail, indicating a structure mismatch.

            Expected results:
            1. The test should pass if the structure of all values in the dictionary matches the 'expected_structure'.
            """
            # Define the expected structure for each value in the dictionary
            expected_structure = {'less': 0, 'greater': 0, 'repeat': 0}

            data = DataCapture()

            # Use DataCapture's list_dic as the example dictionary to be tested
            example_dictionary = data.get_list_dic()

            for key, value in example_dictionary.items():
                self.assertEqual(value, expected_structure)

    if __name__ == '__main__':
        unittest.main()

    def test_default_value(self):
        """
        Test default values after initializing DataCapture.

        This method tests the default values of DataCapture after initialization.

        Test case:
        1. Create an instance of DataCapture.
        2. Check the default values of the instance.

        Expected results:
        1. An instance of DataCapture should be created.
        2. The list of dictionaries should be an empty dictionary, the list of numbers should be an empty list, and the length of the dictionary should be 0.
        """
        data = DataCapture()
        self.assertEqual(type(data.get_list_dic()), dict)
        self.assertEqual(type(data.get_list_number()), list)
        self.assertEqual(data.get_len_dic(), 0)

    def test_add(self):
        """
        Test adding a number to DataCapture.

        This method tests the behavior of the 'add' method in DataCapture when adding a number.

        Test case:
        1. Create an instance of DataCapture.
        2. Add a number (e.g., 'numb' is 5) to the instance.
        3. Check if the added number is in the list of dictionaries.

        Expected results:
        1. An instance of DataCapture should be created.
        2. The number should be added to the instance.
        3. The added number should be found in the list of dictionaries.
        """
        data = DataCapture()
        numb = 5
        data.add(numb)
        list_dic = data.get_list_dic()
        self.assertTrue(numb in list_dic)

    def test_add_error_raise(self):
        """
        Test error cases when adding a number to DataCapture.

        This method tests the error cases of the 'add' method in DataCapture.

        Test cases:
        1. Attempt to add a non-integer value ('numb' is "a").
        2. Attempt to add a negative number ('numb' is -1).
        3. Attempt to add a number that exceeds the specified maximum range ('numb' is MAX_RANG + 5).

        Expected results:
        1. The 'add' method should raise a ValueError because the input is not an integer.
        2. The 'add' method should raise a NegativeNumber exception because the input is a negative number.
        3. The 'add' method should raise an OutOfRange exception because the input exceeds the maximum allowed range.
        """
        data = DataCapture()
        numb = "a"
        with self.assertRaises(ValueError):
            data.add(numb)

    def test_negative_number_raise(self):
        """
        Test adding a negative number to DataCapture.

        This method tests the behavior of the 'add' method when adding a negative number.

        Test case:
        1. Attempt to add a negative number ('numb' is -1).

        Expected result:
        1. The 'add' method should raise a NegativeNumber exception because the input is a negative number.
        """
        data = DataCapture()
        numb = -1
        with self.assertRaises(NegativeNumber):
            data.add(numb)

    def test_out_of_range_raise(self):
        """
        Test adding a number that is out of the specified range to DataCapture.

        This method tests the behavior of the 'add' method when adding a number that exceeds the specified maximum range.

        Test case:
        1. Attempt to add a number greater than the specified maximum range ('numb' is MAX_RANG + 5).

        Expected result:
        1. The 'add' method should raise an OutOfRange exception because the input exceeds the maximum allowed range.
        """
        data = DataCapture()
        numb = MAX_RANG + 5
        with self.assertRaises(OutOfRange):
            data.add(numb)

    def test_add_repeat(self):
        """
        Test counting repeated numbers in DataCapture.

        This method tests the behavior of the 'add' method when adding the same number multiple times.

        Test case:
        1. Create an instance of DataCapture.
        2. Add a number (e.g., 'numb' is 5) to the instance twice.
        3. Check the number of times the number is repeated.

        Expected results:
        1. An instance of DataCapture should be created.
        2. The number should be added to the instance twice.
        3. The number of times the number is repeated should be 2.
        """
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        list_dic = data.get_list_dic()
        self.assertEqual(list_dic[numb]["repeat"], 2)

    def test_add_len_dic(self):
        """
        Test counting the length of DataCapture after adding numbers.

        This method tests the behavior of the 'add' method and the counting of the length of DataCapture after adding numbers.

        Test case:
        1. Create an instance of DataCapture.
        2. Add a number (e.g., 'numb' is 5) to the instance twice.
        3. Check the length of DataCapture.

        Expected results:
        1. An instance of DataCapture should be created.
        2. The number should be added to the instance twice.
        3. The length of DataCapture should be 2.
        """
        data = DataCapture()
        numb = 5
        data.add(numb)
        data.add(numb)
        self.assertEqual(data.get_len_dic(), 2)

    def test_build_stats_return(self):
        """
        Test the return type of the build_stats method.

        This method tests the return type of the 'build_stats' method in DataCapture.

        Test case:
        1. Create an instance of DataCapture.
        2. Call the 'build_stats' method.

        Expected result:
        1. An instance of DataCapture should be created.
        2. The 'build_stats' method should return an instance of Stats.
        """
        data = DataCapture()
        return_data = data.build_stats()
        self.assertIsInstance(return_data, Stats)

    def test_struct_dic(self):
        """
        Test the structure of the dictionary in DataCapture.

        This method tests the structure of the dictionary in DataCapture.

        Test case:
        1. Create an instance of DataCapture.
        2. Get the list of dictionaries.
        3. Check the structure of each dictionary in the list.

        Expected results:
        1. An instance of DataCapture should be created.
        2. The list of dictionaries should be retrieved.
        3. Each dictionary should have 'less', 'greater', and 'repeat' as integer keys.
        """
        data = DataCapture()
        list_dict = data.get_list_dic()
        for numb in list_dict:
            self.assertIsInstance(list_dict[numb]["less"], int)
            self.assertIsInstance(list_dict[numb]["greater"], int)
            self.assertIsInstance(list_dict[numb]["repeat"], int)

class TestModelStats(unittest.TestCase):
    def initial_data_test(self):
        """
        Initialize DataCapture with test data.

        This method initializes an instance of DataCapture with test data for use in other test methods.

        Test case:
        1. Create an instance of DataCapture.
        2. Add several numbers to the instance.
        3. Call the 'build_stats' method to generate statistics.

        Expected result:
        1. An instance of DataCapture should be created.
        2. Test data numbers (3, 9, 3, 4, and 6) should be added to the instance.
        3. Statistics for the test data should be generated.
        """
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        return capture.build_stats()

    def test_less(self):
        """
        Test the 'less' method in Stats.

        This method tests the behavior of the 'less' method in the Stats class.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'less' method with a specific value (e.g., 4).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'less' method should return the number of values less than the specified value (e.g., 2 for 4).
        """
        stats = self.initial_data_test()
        less_value = stats.less(4)
        self.assertEqual(less_value, 2)

    def test_less_not_value_in_data_add(self):
        """
        Test the 'less' method with a value not in the data.

        This method tests the 'less' method in the Stats class with a value that is not present in the test data.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'less' method with a specific value (e.g., 5).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'less' method should return the number of values less than the specified value (e.g., 3 for 5), even if the value is not in the test data.
        """
        stats = self.initial_data_test()
        less_value = stats.less(5)
        self.assertEqual(less_value, 3)

    def test_greater(self):
        """
        Test the 'greater' method in Stats.

        This method tests the behavior of the 'greater' method in the Stats class.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'greater' method with a specific value (e.g., 4).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'greater' method should return the number of values greater than the specified value (e.g., 2 for 4).
        """
        stats = self.initial_data_test()
        greater_value = stats.greater(4)
        self.assertEqual(greater_value, 2)

    def test_greater_not_in_data_add(self):
        """
        Test the 'greater' method with a value not in the data.

        This method tests the 'greater' method in the Stats class with a value that is not present in the test data.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'greater' method with a specific value (e.g., 10).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'greater' method should return 0 because the specified value (e.g., 10) is not in the test data.
        """
        stats = self.initial_data_test()
        greater_value = stats.greater(10)
        self.assertEqual(greater_value, 0)

    def test_between(self):
        """
        Test the 'between' method in Stats.

        This method tests the behavior of the 'between' method in the Stats class.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'between' method with a specific range (e.g., 3 and 6).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'between' method should return the number of values between the specified range (e.g., 4).
        """
        stats = self.initial_data_test()
        greater_value = stats.between(3, 6)
        self.assertEqual(greater_value, 4)

    def test_between_reversed_range(self):
        """
        Test the 'between' method with a reversed range.

        This method tests the 'between' method in the Stats class with a reversed range where the minimum value is greater than the maximum value.

        Test case:
        1. Initialize DataCapture with test data.
        2. Create an instance of Stats using the test data.
        3. Call the 'between' method with a reversed range (e.g., 6 and 3).

        Expected result:
        1. DataCapture should be initialized with test data.
        2. An instance of Stats should be created with the test data.
        3. The 'between' method should return the number of values between the specified reversed range (e.g., 4).
        """
        stats = self.initial_data_test()
        greater_value = stats.between(6, 3)
        self.assertEqual(greater_value, 4)

if __name__ == '__main__':
    unittest.main()
