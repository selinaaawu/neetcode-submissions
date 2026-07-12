# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # ITERATIVE BFS | time: O(n), space: O(n)
        # only return right side view
        # last/rightmost value from each level
        # BFS level order traversal & return last element

        # if tree doesn't exist -> empty list
        if not root:
            return []

        result = []
        queue = deque([root])

        # while queue is not empty
        while queue:
            # empty list of values for current level
            level = []

             # pop node from queue, update rightmost, push left/right children
            for _ in range(len(queue)):
                node = queue.popleft()
                rightmost = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # add rightmsot value
            result.append(rightmost)
        
        return result
        