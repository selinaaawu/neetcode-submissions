# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ## RECURISVE DFS: time: O(n), space: O(h)
        # dfs returns (balanced subtree, height)
        # tree balanced IFF left subtree balanced & right subtree balanced
        #                   & left subtree hight - right subtree height <= 1
        # if one subtree is not balanced, future subtrees aren't balanced either
        # return last balanced subtree boolean
        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)
            difference = abs(left[1] - right[1])
            balanced = left[0] and right[0] and difference <= 1

            return (balanced, 1 + max(left[1], right[1]))
        
        return dfs(root)[0]
