# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Leetcode challenge the description and details about the challenge can be
found in the link https://leetcode.com/problems/two-sum/.

"""
from typing import List


class Solution:
    """Solution class as followed in Leetcode

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """To calculate the two sums challenge

        Args:
            nums: A given list of numbers
            target: Target Number

        Returns:
            A list of index
        """
        if len(nums) == 2:
            return [0, 1]
        for index in range(len(nums)):
            value = nums[index]
            if target - value in nums:
                if index != nums.index(target - value):
                    return sorted([index, nums.index(target - value)])
        return [0]
