"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for i in range(len(num1)):
            result += int(num1[::-1][i]) * 10 ** i
        for i in range(len(num2)):
            result += int(num2[::-1][i]) * 10 ** i
        return '{}'.format(result)