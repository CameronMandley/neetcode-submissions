# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        first = head
        while first:
            count += 1 
            first = first.next
            
        if n == count:
            return head.next
        second = head
        while second and count - n > 1:
            second = second.next
            count -= 1
        
        second.next = second.next.next
        return head
