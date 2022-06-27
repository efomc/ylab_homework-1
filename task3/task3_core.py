from math import log
from math import floor


def zeros(n):
    if n:
        k_max = floor(log(n, 5))
        zeros_list = [floor(n / (5**k)) for k in range(1, k_max + 1)]
    else:
        zeros_list = []
    return sum(zeros_list)
