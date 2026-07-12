# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        # RECURSIVE DFS | time: O(n), space: O(n)
        # inorder traversal gives values in sorted order
        # count elements visited and return once kth element

        count = k
        kth = root.val

        # inorder DFS
        def dfs(node):
            nonlocal count, kth
            if not node:
                return

            # visit left subtree
            dfs(node.left)

            # check if kth element, update kth value, decrement count
            if count == 0:
                return
            kth = node.val
            count -= 1

            # visit right subtree
            dfs(node.right)
        
        dfs(root)
        return kth
        