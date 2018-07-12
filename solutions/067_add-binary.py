"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = 0
        for i in range(len(a)):
            result += int(a[::-1][i]) * 2 ** i
        for i in range(len(b)):
            result += int(b[::-1][i]) * 2 ** i
        return '{:b}'.format(result)