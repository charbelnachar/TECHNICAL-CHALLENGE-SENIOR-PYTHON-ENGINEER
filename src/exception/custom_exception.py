from src.utility.constante import MAX_RANG


class OutOfRange(Exception):

    def __init__(self):
        self.message = f"the list has more than {MAX_RANG} items "
        super().__init__(self.message)