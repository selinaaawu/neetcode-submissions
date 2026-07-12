# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ## ITERATIVE BFS | time: O(n), space: O(n)
        # level order visits level by level
        # list to store levels, queue stores value
        # for length of queue, create new list

        # if tree doesn't exist -> empty list
        if not root:
            return []

        result = []
        queue = deque([root])

        # while queue is not empty
        while queue:
            # empty list of values for current level
            values = []

            # pop node from queue, add value, push left/right children
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add values to result list
            result.append(values)
        
        return result


        
        