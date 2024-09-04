# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum_array = []
        counter = -1
        prev,slow,fast= None,head,head
        while fast and fast.next:   
            prev = slow
            sum_array.append(prev.val)
            slow = slow.next
            fast = fast.next.next
        while slow:
            sum_array[counter] += slow.val
            counter -= 1
            slow = slow.next
        return max(sum_array)