# -*- coding: utf-8 -*-
# pylint: disable=R0201

"""Leetcode challenge for Roman to integer
Description here https://leetcode.com/problems/roman-to-integer/
Found difficult
"""

class Solution:
    """Leetcode format

    """

    def __init__(self):
        self.mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'E': 4,
            'F': 9,
            'G': 40,
            'H': 90,
            'J': 400,
            'K': 900}

    def romantoint(self, roman: str) -> int:
        """Leetcode format

        Args:
            s: String Roman

        Returns:
            An integer value converted from roman value

        """
        if len(roman) == 1:
            return self.mapping[roman]
        roman = roman.replace("CM", "K").replace("CD", "J").replace(
            "XC", "H").replace("XL", "G").replace(
            "IX", "F").replace("IV", "E")
        return sum(map(lambda x: self.mapping[x], roman))
