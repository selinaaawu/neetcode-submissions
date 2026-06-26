# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## LINKED LIST | time: O(n), space: O(1)
        # reverse list and return new beginning of list
        # 0 -> 1 -> 2 -> 3 -> None
        # None <- 0 <- 1 <- 2 <- 3

        prev, curr = None, head
        while curr:
            temp = curr.next    # store next value
            curr.next = prev    # reverse direction
            prev = curr         # update prev
            curr = temp         # update curr

        return prev
        