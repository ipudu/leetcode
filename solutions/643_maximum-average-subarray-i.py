"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        acc_sum = [0]
        s = 0
        for n in nums:
            s += n
            acc_sum.append(s)
        max_average = acc_sum[k] / k
        for i in range(1, len(acc_sum)):
            if i + k <= len(acc_sum):
                max_average = max((acc_sum[i+k-1] - acc_sum[i-1]) / k, max_average)
        return max_average