# -*- coding: utf-8 -*-
# pylint: disable=R0201
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        combined_val = ListNode()
        if l1.val == [] and l2.val == []:
            return ListNode()
        if not l1.next:
            while l1.next:
                combined_val.val = l1.val
                l1 = l1.next
                combined_val = combined_val.next
            return combined_val
        if not l2.next:
            while l2.next:
                combined_val.val = l2.val
                l2 = l2.next
                combined_val = combined_val.next
            return combined_val
        while True:
            if not l1.next or not l2.next:
                break
            else:
                if l1.val > l2.val:
                    combined_val.val = l1.val
                    l1 = l1.next
                    combined_val = combined_val.next
                elif l2.val > l1.val:
                    combined_val.val = l2.val
                    l2 = l2.next
                    combined_val = combined_val.next
                elif l1.val == l2.val:
                    combined_val.val = l1.val
                    l1 = l1.next
                    combined_val = combined_val.next
                    combined_val.val = l2.val
                    l2 = l2.next
                    combined_val = combined_val.next


def create_linkedlist(l1: List) -> ListNode:
    """

    Args:
        l1:

    Returns:

    """
    ll_list = None
    head = None
    for index, value in enumerate(l1):
        if not ll_list:
            ll_list = ListNode(val=value, next=l1[index + 1])
            head = ll_list
            continue
        try:
            ll_list = ListNode(val=value, next=l1[index + 1])
        except IndexError:
            ll_list = ListNode(val=value, next=None)
    return ll_list, head


l1, head1 = create_linkedlist([1, 2, 4])
l1, head2 = create_linkedlist([])

while True:
    print(head1.val)
    head1 = head1.next
    if not head1.next:
        break