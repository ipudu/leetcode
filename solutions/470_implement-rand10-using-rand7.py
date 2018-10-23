"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
"""

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()
        
        while num < 40:
            num = (rand7() - 1) * 7 + rand7()
        
        return num % 10 + 1 