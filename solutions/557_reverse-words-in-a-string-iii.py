"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
            
        return str(' '.join(s_list))