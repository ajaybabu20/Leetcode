# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Leetcode problem the description of the problem is in below link
https://leetcode.com/problems/longest-common-prefix/submissions/
"""
from typing import List


class Solution:
    """Leetcode Template

    """

    def longestcommonprefix(self, strs: List[str]) -> str:
        """
        Longest Prefix function
        Args:
            strs: A list of string to find the longest prefix

        Returns:
            Longest Prefix in the given list
        """
        index = 1
        first = strs[0]
        prefix = ''
        while True:
            for string in strs[1:]:
                if string[0:index] != first[0:index]:
                    return prefix
            prefix += first[index - 1]
            index += 1
            if len(prefix) == len(first):
                return prefix
