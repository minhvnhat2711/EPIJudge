from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    # dynamic programming problem
    can_reach = 0
    for i in range(len(A)):
        if can_reach >= i:
            can_reach = max(can_reach, A[i] + i)
            if can_reach >= len(A)-1: return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
