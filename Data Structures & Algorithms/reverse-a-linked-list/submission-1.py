# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## RECURSIVE
        # base case
        if not head or not head.next:
            return head

        # reverse tail
        newHead = self.reverseList(head.next)

        # append head after
        head.next.next = head
        head.next = None

        return newHead
        
        # ## ITERATIVE
        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev

        