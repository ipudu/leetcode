"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        l = sorted(nums)[::-1]
        for i in range(len(l)):
            if i == 0:
                d[l[i]] = "Gold Medal"
            elif i == 1:
                d[l[i]] = "Silver Medal"    
            elif i == 2:
                d[l[i]] = "Bronze Medal"
            else:
                d[l[i]] = str(i+1) 
        result = []
        for n in nums:
            result.append(d[n])
        return result