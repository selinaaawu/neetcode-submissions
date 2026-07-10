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
        if not p and not q:
            return True
        
        # check if parents are same
        # print(p.val, q.val)
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False
        