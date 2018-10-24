"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        length = 1
        result = ''
        while length <= min([len(s) for s in strs]):
            for i in range(1, len(strs)):
                if strs[i][:length] != strs[i-1][:length]:
                    return result
            result = strs[0][:length]
            length += 1
        return result