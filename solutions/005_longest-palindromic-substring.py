"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        def polindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            p1 = polindrome(s, i, i)
            if len(p1) > len(result):
                result = p1
            p2 = polindrome(s, i, i+1)
            if len(p2) > len(result):
                result = p2
        
        return result