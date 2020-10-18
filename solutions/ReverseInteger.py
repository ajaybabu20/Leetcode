# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Leetcode challenge for Reverse string.
Details can be found here
https://leetcode.com/problems/reverse-integer/submissions/

"""


class Solution:
    """Solution class as followed in Leetcode

       """
    def reverse(self, val: int) -> int:
        """Function to reverse integer

        Args:
            val: An int value

        Returns: Reversed integer

        """
        result = int(str(abs(val))[::-1])
        if result > 2147483647:
            return 0
        if val < 0:
            return -result
        return result
