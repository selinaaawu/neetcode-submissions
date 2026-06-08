# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        
        i = 0
        while i < n:
            i += 1
            second = second.next
        
        if second is None:
            return head.next
        
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next

        return head



        