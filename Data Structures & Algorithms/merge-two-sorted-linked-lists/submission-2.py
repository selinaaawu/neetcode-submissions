# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## RECURSIVE
        # base case = end of 
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


        # ## ITERATIVE
        # dummy = ListNode()
        # curr = dummy
        
        # while list1 and list2:
        #     # list1 value smaller
        #     if list1.val < list2.val:
        #         # append list1
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         # append list2
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next
        
        # # append whichever list still has elements
        # curr.next = list1 or list2
        # return dummy.next
        