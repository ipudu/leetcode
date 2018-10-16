"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = l1
        carry_over = 0
        while True:
            if l2:
                l1.val += l2.val
                l2 = l2.next
            l1.val += carry_over
            carry_over = l1.val // 10
            l1.val %= 10

            if not l1.next:
                if not l2 and carry_over == 0: 
                    break
                l1.next = ListNode(0)
            l1 = l1.next                
        return start