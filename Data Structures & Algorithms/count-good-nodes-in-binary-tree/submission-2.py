# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        ## RECURSIVE DFS | time: O(n), space: O(n)
        # node is good if no earlier nodes has greater value
        # for every node, save/update max value so far in path
        # if node >= max value -> good node, add 1
        # if ndoe < max value -> bad node, ignore
        # keep track of max value

        def dfs(node, max_value):
            if not node:
                return 0
            
            add = 0
            if node.val >= max_value:
                add = 1

            max_value = max(max_value, node.val)
            left = dfs(node.left, max_value)
            right = dfs(node.right, max_value)
            return add + left + right
            
        return dfs(root, root.val)
        