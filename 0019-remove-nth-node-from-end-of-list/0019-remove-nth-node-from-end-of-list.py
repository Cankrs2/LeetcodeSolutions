# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow,curr = head,head
        while n > 0:
            curr = curr.next
            n-=1

        if curr is None:
            head = head.next
            return head

        while curr.next:
            curr = curr.next
            slow = slow.next
        slow.next = slow.next.next
        return head