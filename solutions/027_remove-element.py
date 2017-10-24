class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == val:
                nums.pop(i)
                j -= 1
            else:
                i += 1