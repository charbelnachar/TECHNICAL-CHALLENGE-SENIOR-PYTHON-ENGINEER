
from src.exception.custom_exception import NegativeNumber
from src.exception.custom_exception import OutOfRange
from src.utility.constante import MAX_RANG


class DataCapture():
    """DataCapture class constructor
                                """
    def __init__(self) -> None:
        # constructor that initializes the object and its variables
        self.list_number = []
        self.list_dic = {}
        self.len_dic = 0
        for num in range(1,MAX_RANG):

            data = {
                    "less"   : 0,
                    "greater": 0,
                    "repeat" : 0
                    }
            self.list_dic[num] = data





    def get_list_number(self) -> list:
        """returns the list of numbers after being processed from the dic
                          :param None.
                          :returns:  list of numbers processed from dec
                          :rtype: List
                          """
        return self.list_number

    def get_list_dic(self) -> list:
        """returns the list of dict
                                  :param None.
                                  :returns:  list of dict
                                  :rtype: List
                                  """
        return self.list_dic

    def get_len_dic(self) -> int:
        """returns len of dic
                                  :param None.
                                  :returns:  len of dict
                                  :rtype: int
                                  """
        return self.len_dic


    def add(self, number:int) -> None :
        """
        Adds the values to the dictionary and sums the quantity

            :param int num1: First number to add.
            :returns:  None.
            :rtype: None.
            :raises OutOfRange: the maximum number of values to be added is passed.
            :raises NegativeNumber: the aggregate number is negative and must be positive.
            """
        try:
            number = int(number)
        except ValueError:
            raise ValueError

        if number<0:
            raise NegativeNumber

        if number <= MAX_RANG:

            self.list_dic[number]["repeat"] += 1
            self.len_dic += 1
        else:
            raise OutOfRange




    def build_stats(self) -> "Stats":
        """Generates statistics.
                    :param : None
                    :returns:  object type stats where they have the methods to handle the information .
                    :rtype: Stats
        """

        self.list_number = sorted(self.list_dic)
        aux_greater = self.len_dic
        aux_less = 0
        for value in self.list_number:
            aux_greater = aux_greater - self.list_dic[value]["repeat"]
            self.list_dic[value]["less"] =aux_less
            self.list_dic[value]["greater"] = aux_greater
            aux_less = self.list_dic[value]["repeat"] + aux_less

        stats = Stats(self.list_dic,self.len_dic)
        return stats


class Stats():

    def __init__(self,list_dic = None ,len_dic = None):
        """Stats class constructor
                            :param int numb: number to check in the statistics.
                            """
        if list_dic != None and len_dic != None :
            self.list_dic = list_dic
            self.len_dic = len_dic
        else:
            self.list_dic = {}
            self.len_dic = 0


    def less(self, numb:int) -> int:
        """returns the number of numbers less than the value passed in
                    :param int numb: number to check in the statistics.
                    :returns:  number of values less than numb.
                    :rtype: Int
                    :raises KeyError: the value is not in the list.
                    """

        return  self.list_dic[numb]["less"]

    def greater(self, numb:int) -> int:
        """returns the number of numbers greater than the value passed in
                          :param int numb: number to check in the statistics.
                          :returns:  number of values greater than numb.
                          :rtype: Int
                          :raises KeyError: the value is not in the list.
                          """

        return self.list_dic[numb]["greater"]

    def between(self, numb:int, numb2:int) -> int :
        """returns the number of numbers that belong to the passed range
                          :param int numb: number to check in the statistics.
                          :param int numb2: number to check in the statistics.
                          :returns: returns the number of numbers between numb and numb2.
                          :rtype: Int
                          :raises KeyError: the value is not in the list.
                          """
        if numb < numb2:
            min, max = numb, numb2
        else:
            min, max = numb2, numb

        return self.len_dic - self.list_dic[min]["less"] - self.list_dic[max]["greater"]

