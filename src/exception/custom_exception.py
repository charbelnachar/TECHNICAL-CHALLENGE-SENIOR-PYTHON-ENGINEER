from src.utility.constante import MAX_RANG


class OutOfRange(Exception):

    def __init__(self,number):
        self.message = f"the {number} does not fall within the range of 1 to  {MAX_RANG} "
        super().__init__(self.message)

class NegativeNumber(Exception):

    def __init__(self,number):
        self.message = f"{number} is negative and must be positive"
        super().__init__(self.message)