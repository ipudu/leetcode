"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
https://leetcode.com/static/images/problemset/keyboard.png

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

"""

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        result = []
        
        for word in words:
            a, b, c = 0, 0, 0
            for w in word:
                if w in 'QWERTYUIOPqwertyuiop':
                    a = 1
                elif w in 'ASDFGHJKLasdfghjkl':
                    b = 1
                else:
                    c = 1
            if a + b + c == 1:
                result.append(word)
        
        return result