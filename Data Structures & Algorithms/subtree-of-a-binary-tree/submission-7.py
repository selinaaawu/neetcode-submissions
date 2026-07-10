# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # compare value of subtree with value in root
        # if value in subtree == value in root -> start checking
        # check node & value for all nodes/values in subroot
        # if everything matches -> return True
        # else no subtree -> return False

        # check if node & values same
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            
            return False
        
        if not root:
            return False

        if not subRoot:
            return True

        if dfs(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        
        return False

        