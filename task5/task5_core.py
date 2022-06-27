from math import log, ceil, prod
from itertools import combinations_with_replacement


def count_find_num(primesL, limit):
    result = []
    result_dict = dict()
    min_prime = min(primesL)
    first_number = prod(primesL)
    if first_number <= limit:
        additional_part = limit // first_number
        additional_positions = ceil(log(additional_part, min_prime))
        additional_list = []
        for stage in range(1, additional_positions):
            additional_list += list(combinations_with_replacement(primesL, stage))
        additional_list = (
            [primesL]
            + [primesL + list(item) for item in additional_list]
            + [primesL + [min_prime] * additional_positions]
        )
        result_dict = {
            prod(item): item for item in additional_list if prod(item) <= limit
        }
    if result_dict:
        result = [len(result_dict), max(result_dict)]
    return result
