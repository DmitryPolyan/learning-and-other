"""
Given a linked list, swap every two adjacent nodes and return its head.
exmpl:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Follow up: Can you solve the problem without modifying the values in the list's nodes?
(i.e., Only nodes themselves may be changed.)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:
            current_node = head
            next_node = current_node.next
            while current_node and next_node:
                current_node.val, current_node.next.val = current_node.next.val, current_node.val
                current_node = current_node.next.next
                if current_node:
                    next_node = current_node.next
                else:
                    break
        return head
