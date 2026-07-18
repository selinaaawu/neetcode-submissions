# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ## HEAP | 
        # minHeap stores (node value, list index, node)
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            # pop smallest value from heap
            value, i, node = heapq.heappop(minHeap)

            # attach to curr
            curr.next = node
            curr = curr.next

            # if smallest node has next node, add to minHeap
            if node and node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next


        ## MERGE ONE BY ONE | time: O(n * k) | space: O(1)
        # merge two sorted lists
        def mergeList(list1, list2):
            root = ListNode()
            curr = root

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
                
                curr.next = list1 or list2
                
            return root.next
        
        if len(lists) == 0:
            return None
        
        # for each list, merge two lsits together, store in next list
        for i in range(1, len(lists)):
            lists[i] = mergeList(lists[i - 1], lists[i])
        
        return lists[-1]

        # ## ITERATION | time: O(n * k), space: O(1)
        # # pick smallest head node among all lists
        # root = ListNode(0)
        # curr = root
        
        # while True:
        #     # find which list contains smallest value
        #     minList = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if minList == -1 or lists[i].val < lists[minList].val:
        #             minList = i
            
        #     # if all lists are empty, finished
        #     if minList == -1:
        #         break
            
        #     curr.next = lists[minList]              # attach smallest node
        #     lists[minList] = lists[minList].next    # move list pointer forward
        #     curr = curr.next                        # move curr pointer forward
        
        # return root.next

        # ## BRUTE FORCE | time: O(n log n), space: O(n)
        # # collect every value & sort
        # nodes = []
        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        #         lst = lst.next
        # nodes.sort()

        # # rebuild linked list 
        # root = ListNode(0)
        # curr = root
        # for node in nodes:
        #     curr.next = ListNode(node)
        #     curr = curr.next
        # return root.next
        