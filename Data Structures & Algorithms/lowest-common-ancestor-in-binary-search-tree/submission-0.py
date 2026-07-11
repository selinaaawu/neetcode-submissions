# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ## RECURISVE: time: O(h), space: O(h)
        if not root or not p or not q:
            return None

        # both values smaller than curr -> value in left subtree
        # if max(p.val, q.val) < root.val:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # both values greater than curr -> value in right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # split point indicates lowest common ancestor !!!!
        else: 
            return root
        
        ## ITERATIVE | time: O(h), space: O(1)
        # if p < curr & q < curr -> value in left subtree
        # if p  > curr & q > curr -> value in right subtree
        # if split -> curr node is LCA
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val < curr.val:
                curr = curr.right
            else:
                return curr
        