from src.utility.constante import MAX_RANG


class OutOfRange(Exception):

    def __init__(self):
        self.message = f"the list has more than {MAX_RANG} items "
        super().__init__(self.message)

class NegativeNumber(Exception):

    def __init__(self):
        self.message = f"the aggregate number is negative and must be positive"
        super().__init__(self.message)