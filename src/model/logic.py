import time

from src.exception.custom_exception import OutOfRange
from src.utility.constante import MAX_RANG


class DataCapture():
    def __init__(self) -> None:
        # constructor that initializes the object and its variables
        self.list_number = []
        self.list_dic = {}
        self.len_dic = 0

    def get_list_number(self):
        return  self.list_number

    def get_list_dic(self):
        return self.list_dic

    def get_len_dic(self):
        return self.len_dic


    def add(self, number) -> None :
        # adds the values to the dictionary and sums the quantity
        if number in self.list_dic:
            self.list_dic[number]["repeat"] += 1
        else:
            data = {
                    "less":0,
                    "greater":0,
                    "repeat":1
                    }
            self.list_dic[number]=data
        self.len_dic += 1

        if self.len_dic <= MAX_RANG:
            self.list_number.append(number)
        else:
            raise OutOfRange


    def sorted_dic_to_list(self) -> None:
        # sort and return a list of numbers
        self.list_number =  sorted(self.list_dic)

    def build_stats(self) -> "self objetc":
        # generates statistics 
        aux_greater = self.len_dic
        aux_less = 0
        for value in self.list_number:
            aux_greater = aux_greater - self.list_dic[value]["repeat"]
            self.list_dic[value]["less"] = aux_less
            self.list_dic[value]["greater"] = aux_greater
            aux_less = self.list_dic[value]["repeat"] + aux_less
        return self

    def less(self, numb) -> int:
        # returns the number of numbers less than the value passed in
        return  self.list_dic[numb]["less"]

    def greater(self, numb) -> int:
        # returns the number of numbers greater than the value passed in
        return self.list_dic[numb]["greater"]

    def between(self, numb, numb2) -> int :
        # returns the number of numbers that belong to the passed range
        return self.len_dic - self.list_dic[numb]["less"] - self.list_dic[numb2]["greater"]

