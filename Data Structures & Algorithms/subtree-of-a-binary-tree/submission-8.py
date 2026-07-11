# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        ## RECURSIVE DFS | time: O(m * n), space: O(m + n)
        # walk through every node of root tree
        # check if subtree starting at root is same as subroot
        # compare both subtrees fully, if identical -> subtree found
        # otherwise -> continue searching left/right children

        # check if root and subroot are the same
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                left = sameTree(root.left, subRoot.left)
                right = sameTree(root.right, subRoot.right)
                return left and right

            return False
        
        # nothing in root -> cannot contain subroot
        if not root:
            return False

        # nothing in subroot -> always True
        if not subRoot:
            return True

        # compare every root & subroot for matching
        if sameTree(root, subRoot):
            return True
        # check smaller subroots of tree
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        
        return False
        