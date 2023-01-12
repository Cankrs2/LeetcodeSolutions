# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast,slow = head,head
        while n > 0:
            fast = fast.next
            n -=1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if slow == head and not fast:
            return head.next
        slow.next = slow.next.next
        return head

        