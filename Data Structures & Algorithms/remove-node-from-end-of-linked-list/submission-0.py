# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        if n == length:
            return head.next
        
        node = head
        for _ in range(length - n - 1):
            node = node.next
        node.next = node.next.next

        return head