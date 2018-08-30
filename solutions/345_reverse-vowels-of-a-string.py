"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        p1 = 0
        p2 = len(s) - 1
        l = list(s)
        
        while p1 < p2:
            if l[p1] in vowels and l[p2] in vowels:
                l[p1], l[p2] = l[p2], l[p1]
                p1 += 1
                p2 -= 1
            elif l[p1] in vowels:
                p2 -= 1
            elif l[p2] in vowels:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1
        return ''.join(l)