# -*- coding: utf-8 -*-
# pylint: disable=R0201
"""Leetcode problem the description of the problem is in below link
https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        point1 = head
        point2 = head.next
        while point1:
            if point1 == point2:
                return True
            else:
                point1 = point1.next
                point2 = point2.next
        return True

