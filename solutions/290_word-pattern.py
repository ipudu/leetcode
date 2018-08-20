"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        uniq = set(pattern)
        index = []
        
        for u in uniq:
            tmp = []
            for i in range(len(pattern)):
                if pattern[i] == u:
                    tmp.append(i)
            index.append(tmp)
        l = string.split(' ')
        if len(l) == 1 and len(index) != 1:
            return False
        
        length = sum([len(i_list) for i_list in index])
        if length != len(l):
            return False
        
        seen = set()
        for i_list in index:
            for i in range(len(i_list)):
                seen.add(l[i_list[i]])
                if l[i_list[i]] != l[i_list[0]]:
                    return False
        
        if len(seen) != len(index):
            return False
        
        return True