"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        for n in nums1:
            if not n in d.keys():
                d[n] = 1
        for n in nums2:
            if n in d.keys():
                d[n] += 1
        result = []
        for key, value in d.items():
                if value >= 2:
                    result.append(key)
        return result