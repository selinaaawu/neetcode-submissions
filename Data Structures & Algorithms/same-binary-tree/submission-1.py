# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # binary trees are same if identical structure & identical values
        #   both nodes are null -> match, True
        #   one node null       -> mismatch, False
        #   values differ       -> mismatch, False

        ## RECURSIVE DFS
        # both nodes are null -> match
        if not p and not q:
            return True

        # oen node is null OR values differ -> mismatch
        if not p or not q or p.val != q.val:
            return False
        
        # check if parents are same
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
        