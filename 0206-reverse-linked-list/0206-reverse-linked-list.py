# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        while head != None:
            b = head
            head = head.next
            b.next = a
            a=b
            
        head = a
        return head