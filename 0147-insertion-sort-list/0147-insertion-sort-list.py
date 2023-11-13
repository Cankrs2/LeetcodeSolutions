# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1000000000,head)
        prev = dummy
        current = head
        while current != None:
            temp = dummy
            while temp.next.val < current.val and temp.next != None:
                temp = temp.next
            if prev == temp:
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current.next = temp.next
                temp.next = current
                current = prev.next
                
        return dummy.next
                