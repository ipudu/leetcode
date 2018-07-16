"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 1
        while i ** 2 < c:
            i += 1
        n = i + 1
        
        for i in range(n):
            for j in range(n):
                if i ** 2 + j ** 2 == c:
                    return True
        return False