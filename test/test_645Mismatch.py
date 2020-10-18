"""Actual Test conditions in Leetcode for our MismatchProblem.
The testing done using pytest, and automated using tox.

"""
from solutions.SetMismatch import Solution


def test_numberone():
    nums = [1, 2, 2, 4]
    expected = [2, 3]
    result = Solution().finderrornums(nums=nums)
    assert result == expected


def test_numbertwo():
    nums = [1, 1]
    expected = [1, 2]
    result = Solution().finderrornums(nums=nums)
    assert result == expected
