from src.exception.custom_exception import NegativeNumber
from src.exception.custom_exception import OutOfRange
from src.utility.constante import MAX_RANG


def valid_number(number):
    """

       This method validates the input number.

       :param int number: The number to be validated and added to the data dictionary.
       :return: The valid number.
       :rtype: int
       :raises ValueError: If the provided value is not a valid integer.
       :raises OutOfRange: If the number exceeds the maximum allowed range (MAX_RANG).
       :raises NegativeNumber: If the number is negative, it must be positive.
       """

    try:
        number = int(number)
    except ValueError:
        raise ValueError(f'{number} is not a valid number')

    if number < 0:
        raise NegativeNumber(number)

    if number <= MAX_RANG:
        return number

    else:
        raise OutOfRange(number)


class DataCapture():
    """DataCapture class constructor
                                """

    def __init__(self) -> None:
        # constructor that initializes the object and its variables
        # self.list_number = {}
        # self.list_dic = {num: {"less": 0, "greater": 0, "repeat": 0} for num in range(1, MAX_RANG)}
        # self.len_dic = 0
        self.list_dic = {}
        self.len_dic = 0

    def add(self, number: int) -> None:
        """
            Adds a number to the data dictionary while maintaining quantity information.

            This method adds a number to the data dictionary while keeping track of the quantity of occurrences of
            each number.

            :param int number: The number to be added to the data dictionary.
            :return: None.
            :rtype: None
            :raises ValueError: The provided value is not a valid number
            :raises OutOfRange: the maximum number of values to be added is passed.
            :raises NegativeNumber: the aggregate number is negative and must be positive.
            """
        number = valid_number(number)
        if number in self.list_dic:
            self.list_dic[number]["repeat"] += 1
        else:
            self.list_dic[number] = {"less": 0, "greater": 0, "repeat": 1}
            self.len_dic += 1

    def build_stats(self) -> "Stats":
        """
           This method generates statistics from the data dictionary, creating a Stats object
           that provides methods for handling statistical information.

           :param None: No parameters are needed.
           :returns: An object of type 'Stats' with methods for handling statistical information.
           :rtype: Stats
           """

        stats = Stats()

        aux_greater = self.len_dic
        aux_less = 0

        for number in range(1, MAX_RANG + 1):
            data = self.list_dic.get(number, {"less": 0, "greater": 0, "repeat": 0})
            stats.list_dic[number] = {
                    "less"   : aux_less,
                    "greater": aux_greater,
                    "repeat" : data["repeat"]
                    }
            aux_greater -= data["repeat"]
            aux_less += data["repeat"]

        stats.len_dic = self.len_dic

        return stats


class Stats():

    def __init__(self, list_dic=None, len_dic=None):
        """Stats class constructor
                            :param int numb: number to check in the statistics.
                            """
        if list_dic != None and len_dic != None:
            self.list_dic = list_dic
            self.len_dic = len_dic
        else:
            self.list_dic = {}
            self.len_dic = 0

    def less(self, numb: int) -> int:
        """returns the number of numbers less than the value passed in
                    :param int numb: number to check in the statistics.
                    :returns:  number of values less than numb.
                    :rtype: Int
                    :raises ValueError: The provided value is not a valid number
                    :raises OutOfRange: the maximum number of values to be added is passed.
                    :raises NegativeNumber: the aggregate number is negative and must be positive.

                    """
        valid_number(numb)
        return self.list_dic[numb]["less"]

    def greater(self, numb: int) -> int:
        """returns the number of numbers greater than the value passed in
            :param int numb: number to check in the statistics.
            :returns:  number of values greater than numb.
            :rtype: Int
            :raises ValueError: The provided value is not a valid number
            :raises OutOfRange: the maximum number of values to be added is passed.
            :raises NegativeNumber: the aggregate number is negative and must be positive.

                          """
        valid_number(numb)
        return self.list_dic[numb]["greater"]

    def between(self, numb: int, numb2: int) -> int:
        """returns the number of numbers that belong to the passed range
                          :param int numb: number to check in the statistics.
                          :param int numb2: number to check in the statistics.
                          :returns: returns the number of numbers between numb and numb2.
                          :rtype: Int
                          :raises ValueError: The provided value is not a valid number
                          :raises OutOfRange: the maximum number of values to be added is passed.
                          :raises NegativeNumber: the aggregate number is negative and must be positive.

                          """
        valid_number(numb)
        valid_number(numb2)
        if numb < numb2:
            min, max = numb, numb2
        else:
            min, max = numb2, numb

        return self.len_dic - self.list_dic[min]["less"] - self.list_dic[max]["greater"]
