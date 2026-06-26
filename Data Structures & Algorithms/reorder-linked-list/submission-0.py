# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## LINKED LIST
        # 1. detect middle
        # 2. reverse second half
        # 3. merge

        # detect middle
        # [0 1 2 3 4 5 6]
        #        M     T
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next            # middle value
            fast = fast.next.next

        # reverse second half
        # [0 1 2 | 3 4 5 6]
        # [0 1 2 | 3 6 5 4]
        second = slow.next 
        slow.next = None

        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        # prev stores T
        # curr stores null

        # merge two halves
        # [0 1 2]
        # [6 5 4 3]
        # [0 6 1 5 2 4 3]

        first, second = head, prev
        while second:
            # save next pointers
            temp1, temp2 = first.next, second.next

            # add two pointers
            first.next = second
            second.next = temp1

            # update pointers
            first, second = temp1, temp2

