from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    if len(num1) == 0 or len(num2) == 0:
        return []
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num2))):
        for j in reversed(range(len(num1))):
            result[i + j + 1] += (num1[j]*num2[i])
            result[i + j] += result[i + j + 1] // 10      
            result[i + j + 1] %= 10
    result = result[next((i for i, v in enumerate(result) if v > 0), len(result)):] or [0]
    return [sign*result[0]] + result[1:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
