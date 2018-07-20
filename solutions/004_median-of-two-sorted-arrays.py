"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        l= []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1
        
        l.extend(nums1[i:] + nums2[j:])
        if len(l) % 2 == 0:
            return (l[int(len(l)/2)] + l[int(len(l)/2)-1]) / 2
        else:
            return l[int(len(l)/2)]