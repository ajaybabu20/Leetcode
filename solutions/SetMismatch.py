# -*- coding: utf-8 -*-
"""Leetcode problem details are in the below link

https://leetcode.com/problems/set-mismatch/submissions/

The running time of this task is O(n^2) worst case scenario.

"""
from typing import List
from collections import Counter


class Solution:
    """Provide class to define our functions/logic.
    """

    def findErrorNums(self, nums: List[int]) -> List:
        """Provided function to define our logic and to get the result.

        Args:
            nums: The provided error data.

        Returns:
            A list which provides required answer.

        """
        repeated = Counter(nums).most_common()[0][0]
        for i in range(1, len(nums)+1):
            if nums[i-1] != i:
                missing = i
                break
        return [repeated, missing]
