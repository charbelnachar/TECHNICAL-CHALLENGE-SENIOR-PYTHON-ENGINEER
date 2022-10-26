from model.logic import DataCapture
from utility.utility import Utility

capture = DataCapture()
utility = Utility()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
capture.sorted_dic_to_list()
stats = capture.build_stats()
print(stats.less(4))
min,max = utility.order_min_max(3, 6)
print(stats.between(min,max))
print(stats.greater(4))
