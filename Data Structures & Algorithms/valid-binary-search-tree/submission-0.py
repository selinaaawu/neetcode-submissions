# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # RECRUSIVE DFS | time: O(n), space: O(n)
        # left node must be smaller than curr node
        # but greater than higher nodes
        # right node must be greater than curr node
        # but less than higher nodes

        def dfs(node, low, high):
            if not node:
                "done"
                return True
            
            inrange = True if low < node.val < high else False
            if not inrange:
                return False
            print(node.val, low, high)
            print(inrange)

            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return left and right

        return dfs(root, float('-inf'), float('inf'))
        