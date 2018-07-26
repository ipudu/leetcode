# 451 Sort Characters By Frequency 按字母频率排序 

#### 问题描述

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

#### 中文释义

给定一个字符串，按字母出现频率以降序的方式重新排列。频率大的要在频率小的前面，频率相同的的字母，前后顺序无所谓。

#### 解题思路

##### 方法 1

以字典的形式记录字母以及字母的出现的频率。然后相对于字典的value对其进行降序排序。按序排列vaule个对应的key即可。

```python
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        result  = ''
        
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1
        
        for c in sorted(d, key=d.get)[::-1]:
            result += c * d[c]
        
        return result
```