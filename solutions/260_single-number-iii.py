"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}
        
        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
                
        result = []
        
        for key, value in d.items():
            if value == 1:
                result.append(key)
                
        return result