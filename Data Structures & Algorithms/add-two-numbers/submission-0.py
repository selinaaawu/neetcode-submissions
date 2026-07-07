# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ## ITERATION | time: O(max(m, n)), space: O(max(m, n))
        # while more digits exist:
        #   add two digits and carry (if exists)
        #   save remainder (sum % 10) into new node
        #   update carry (sum // 10)
        dummy = ListNode()      # build new lsit
        curr = dummy            # add to this pointer

        carry = 0
        # handles lists of different lengths & final carries
        while l1 or l2 or carry:
            first = l1.val if l1 else 0 
            second = l2.val if l2 else 0 

            sum = first + second + carry
            carry = sum // 10
            digit = sum % 10
            curr.next = ListNode(digit)

            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
