"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
        s = sorted(list(set(nums)))
        result = 0
        for i in range(1, len(s)):
            if s[i] - s[i-1] == 1:
                result = max(result, d[s[i]] + d[s[i-1]])
        return result