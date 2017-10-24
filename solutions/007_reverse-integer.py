"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            result = int('-' + str(x)[:0:-1])
        else:
            result = int(str(x)[::-1])

        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result