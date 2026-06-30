# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ## LINKED LIST | time: O(n), space: O(1)
        # 1. find middle of linked list using slow/fast pointers
        # 2. reverse second half of list (breaking halves apart)
        # 3. merge two halves one-by-one (first then second)

        # find middle
        # [0 1 2 3 4 5 6]
        #        M     T
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next            # slow = middle value 
            fast = fast.next.next       # fast = null

        # reverse second half
        # [0 1 2 3 | 4 5 6]
        # [0 1 2 3 ] [ 6 5 4]
        #  H              T
        curr = slow.next            # start from second half
        prev = slow.next = None     # SPLIT list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        # merge two lists
        # [0 1 2 3 | 6 5 4]
        # [0 6 1 5 2 4 3]
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next  # save next pointers
            first.next = second                     # add first half
            second.next = temp1                     # add second half
            first, second = temp1, temp2            # update pointers
