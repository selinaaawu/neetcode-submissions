# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # ## RECURSIVE DFS | time: O(n), space: O(n)
        # # recurisively compute depth of left & right subtree
        # # return depth = 1 + max(left subtree, right subtree)
        # # bottom up: need info from children

        # if not root:
        #     return 0
        
        # left = self.maxDepth(root.left)     # compute left depth
        # right = self.maxDepth(root.right)   # compute right depth

        # # depth = 1 + max depth of left/right subtree
        # return 1 + max(left, right)

        # ## ITERATIVE DFS: 
        # # stack stores (node, depth)
        # # pop stsack, update max depth, push left/right children with depth + 1
        # if not root: 
        #     return 0
        
        # stack = [(root, 1)]
        # maxDepth = 0

        # while stack:
        #     node, depth = stack.pop()
        #     maxDepth = max(maxDepth, depth)
            
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        
        # return maxDepth

        ## BFS l
        # level order would be good if we see how much levels 
        # we get to and # level = depth
        if not root: 
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            size = len(queue)
            depth += 1

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return depth





        