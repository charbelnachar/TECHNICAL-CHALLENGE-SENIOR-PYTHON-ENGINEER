class Utility():
    def order_min_max(self, numb1, numb2) -> int:
        # sorts and returns in order which is the largest and which is the smallest
        if numb1 < numb2:
            min, max = numb1, numb2
        else:
            min, max = numb2, numb1

        return  min,max

