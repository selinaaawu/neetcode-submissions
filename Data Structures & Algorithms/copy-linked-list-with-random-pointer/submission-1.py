"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        ## SPACE OPTIMIZED | time: O(n), space: O(1)
        if head is None:
            return None
            
        # create deep copy of each node & link to next pointer
        original = head
        while original:
            newNode = Node(original.val)    # create new node
            newNode.next = original.next    # new node points to original next node
            original.next = newNode         # original node points to new node
            original = newNode.next         # work on next original node
        
        # link node to random pointer
        original = head
        while original:
            if original.random:
                original.next.random = original.random.next
            original = original.next.next
        
        # unweave the lists
        original = head
        newList = head.next
        while original:
            nextNode = original.next
            original.next = nextNode.next

            if nextNode.next:
                nextNode.next = nextNode.next.next
            original = original.next

        return newList
            
            



        ## HASH MAP (one pass) | time: O(n), space: O(n)
        # hash map automatically creates copy node whenever accessed
        # traverse list to set value + next pointer + random pointer
        oldToCopy = defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        curr = head
        while curr:
            oldToCopy[curr].val = curr.val                  # update value
            oldToCopy[curr].next = oldToCopy[curr.next]     # update next pointer
            oldToCopy[curr].random =oldToCopy[curr.random]  # update random pointer
            curr = curr.next                                # iterate curr node

        return oldToCopy[head]


        ## HASH MAP (two pass) | time: O(n), space: O(n)
        # first pass: create deep copy of each node & store in hash map
        oldToCopy = {None : None}

        curr = head
        while curr:
            newNode = Node(curr.val)        # create new node
            oldToCopy[curr] = newNode       # store in hash map
            curr = curr.next                # iterate curr node

        # second pass: link next & random pointer using hash map
        curr = head
        while curr:
            newNode = oldToCopy[curr]                   # create new node
            newNode.next = oldToCopy[curr.next]         # link next pointer
            newNode.random = oldToCopy[curr.random]     # link random pointer
            curr = curr.next                            # iterate curr node
        
        return oldToCopy[head]
