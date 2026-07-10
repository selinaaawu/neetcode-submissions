# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ## RECURSIVE DFS | time: O(n), space: O(h)
        # diameter = longest path between two nodes
        #          = left subtree height + right subtree height
        # DFS to compute height, tracking max (left + right) seen

        # global answer
        diameter = 0

        # computes height & max diameter
        def dfs(root):
            nonlocal diameter
            if not root: 
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            diameter = max(diameter, leftHeight + rightHeight)

            # must return height NOT diameter
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return diameter
        