# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle of linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #found the middle, now reverse second half
        second = slow.next
        #split the halves
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # weave the halves together
        first, second = head, prev
        while second:
            # save value references
            temp1, temp2 = first.next, second.next
            # weave
            first.next = second
            second.next = temp1
            # advance to next part of list
            first, second = temp1, temp2


        