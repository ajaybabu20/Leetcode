from solutions import MergeTwoSortedLists as Mt
from typing import List


def create_linkedlist(l1: List) -> Mt.ListNode:
    """

    Args:
        l1:

    Returns:

    """
    l_list = Mt.ListNode()
    for value in l1:
        l_list.val = value
        l_list = l_list.next
    return l_list


def test_numberone():
    l1 = create_linkedlist([1, 2, 4])
    l2 = create_linkedlist([1, 3, 4])
    expected = create_linkedlist([1, 1, 2, 3, 4, 4])
    result = Mt.Solution().mergeTwoLists(l1=l1, l2=l2)
    assert expected == result
