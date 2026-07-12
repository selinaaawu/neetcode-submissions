# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ## RECURSIVE DFS
        # traverse every node
        # for every node, save/update max value in path
        # if node > max value -> False, ignore
        # if ndoe < max value -> True, increase count
        # keep track of max value

        def dfs(node, max_value):
            if not node:
                return 0
            
            print(node.val, max_value)

            add = 0
            if node.val >= max_value:
                add = 1

            max_value = max(max_value, node.val)
            left = dfs(node.left, max_value)
            right = dfs(node.right, max_value)
            return add + left + right
            
        return dfs(root, root.val)

        