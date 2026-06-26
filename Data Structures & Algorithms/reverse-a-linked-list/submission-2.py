# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse list and return new beginning of list
        # 0 -> 1 -> 2 -> 3 -> None
        # None <- 0 <- 1 <- 2 <- 3


        cur = head
        prev = None

        while cur:
            nxt = cur.next     # store next value
            cur.next = prev    # reverse direction
            prev = cur          # update prev
            cur = nxt           # update cur
        return prev
        