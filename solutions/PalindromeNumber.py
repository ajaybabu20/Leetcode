# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Leetcode Problem for Palindrome.
Description of the problem https://leetcode.com/problems/palindrome-number/

"""


class Solution:
    """Solution class as used in Leetcode.

    """

    def ispalindrome(self, val: int) -> bool:
        """To check if a given integer is Palindrome

        Args:
            val: Integer value

        Returns:
            A boolean value

        Alternate solution can be

            def is_palindrome(n):
                x, y = n, 0
                f = lambda: (y * 10) + x % 10
                while x > 0:
                    x, y = x//10 , f()
                return y == n
        This does not convert to string.
        """
        if val < 0:
            return False
        return int(str(val)[::-1]) == val
