"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
       
        nums = sorted(nums)
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]
        
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]