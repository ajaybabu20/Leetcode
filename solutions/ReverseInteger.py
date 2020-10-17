"""Leetcode challenge for Reverse string.
Details can be found here
https://leetcode.com/problems/reverse-integer/submissions/

"""


class Solution:
    """Solution class as followed in Leetcode

       """
    def reverse(self, x: int) -> int:
        """Function to reverse integer

        Args:
            x: An int value

        Returns: Reversed integer

        """
        result = int(str(abs(x))[::-1])
        if result > 2147483647:
            return 0
        if x < 0:
            return -result
        return result
