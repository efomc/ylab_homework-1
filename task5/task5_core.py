from math import log, ceil, prod
from itertools import combinations_with_replacement


ASSERT_LIST = [
    {"primesL": [2, 5, 7], "limit": 500, "assert_result": [5, 490]},
    {"primesL": [2, 3], "limit": 200, "assert_result": [13, 192]},
    {"primesL": [2, 5], "limit": 200, "assert_result": [8, 200]},
    {"primesL": [2, 3, 5], "limit": 500, "assert_result": [12, 480]},
    {"primesL": [2, 3, 5], "limit": 1000, "assert_result": [19, 960]},
    {"primesL": [2, 3, 47], "limit": 200, "assert_result": []},
]


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
            additional_list += list(
                combinations_with_replacement(primesL, stage)
            )
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


def main():
    for assert_data in ASSERT_LIST:
        assert (
                count_find_num(assert_data["primesL"], assert_data["limit"])
                == assert_data["assert_result"]
        )


if __name__ == "__main__":
    main()
