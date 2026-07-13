# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # RECRUSIVE DFS | time: O(n), space: O(n)
        # every node must be within valid range of ancestors
        # tighten bounds while moving down tree

        def dfs(node, low, high):
            if not node:
                return True
            
            # if node not betwen low and high -> not valid BST
            if not low < node.val < high:
                return False

            # left subtree w range (low, new node value)
            left = dfs(node.left, low, node.val)

            # right subtree w range (new node value, high)
            right = dfs(node.right, node.val, high)

            return left and right

        # start with root between '-inf' and 'inf'
        return dfs(root, float('-inf'), float('inf'))
        