# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ## RECURSIVE DFS | time: O(n), space: O(n)
        # if current node is null, return null
        if not root:
            return None
        
        # swap left and right children
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)      # invert left subtree
        self.invertTree(root.right)     # invert right subtree
        
        # return current inverted node
        return root


        ## ITERATIVE DFS | time: O(n), space: O(n)
        # if current node is null, return null
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()              # pop node
            
            # swap left and right children
            node.left, node.right = node.right, node.left

            # if left child exists, add to stack
            if node.left:
                stack.append(node.left)
            # if right child exists, add to stsack
            if node.right:
                stack.append(node.right)    
        return root



        ## BFS | time: O(n), space: O(n)
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            node = queue.popleft()          # remove front node

            # swap left and right children
            node.left, node.right = node.right, node.left

            # if left child exists, add to queue
            if node.left:
                queue.append(node.left)
            # if right child exists, add to queue
            if node.right:
                queue.append(node.right)    
        
        # return root as inverted tree
        return root
        