"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = [0 for i in range(1000001)]

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.s[key] == 0:
            self.s[key] = 1
        
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.s[key] == 1:
            self.s[key] = 0

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return True if self.s[key] == 1 else False