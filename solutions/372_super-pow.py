"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
Credits:
Special thanks to @Stomach_ache for adding this problem and creating all test cases.
"""

class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result = 1
        for n in b[::-1]:
            result = result * a ** n % 1337
            a = a ** 10 % 1337
        return result