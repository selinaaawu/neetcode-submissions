# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # only return right side view
        # rightmost value from each level
        # can create BFS level order traversal and return last element

        if not root:
            return []

        rightmost = []
        level_order = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_order.append(level)
            print(level)

        for level in level_order:
            rightmost.append(level[-1])
        
        return rightmost
        