# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Solution for leetcode problem description in below link
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    """Leetcode format

    """
    def isvalid(self, s: str) -> bool:
        """Checks for valid parathensis

        Args:
            s: string for Parentheses values

        Returns:
            Return if the Parentheses combination is valid

        """
        if len(s) == 1:
            return False
        par_stack = []
        for par in s:
            if par in ['(', '{', '[']:
                par_stack.append(par)
            else:
                if len(par_stack) == 0:
                    return False
                prev = par_stack.pop()
                if not self.check_stack(prev=prev, par=par):
                    return False
        if len(par_stack) != 0:
            return False
        return True

    def check_stack(self, prev: str, par: str) -> bool:
        if prev == "(":
            return par == ")"
        elif prev == "{":
            return par == "}"
        return par == "]"
