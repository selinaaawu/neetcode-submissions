# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        ## RECURSIVE DFS (OPTIMAL) | time: O(n), space: O(n)
        self.preIndex = 0
        self.inIndex = 0

        # build subtree until limit value hit
        def dfs(limit):
            # nore more nodes
            if self.preIndex >= len(preorder):
                return None
            # limit value met, subtree complete
            if inorder[self.inIndex] == limit:
                self.inIndex += 1
                return None
            
            # create root node, increment preIndex
            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1

            # left subtree = nodes less than root
            root.left = dfs(root.val)
            # right subtree = nodes greater than root to 'inf'
            root.right = dfs(limit)
            
            return root
        
        return dfs(float('inf'))        


        ## HASHMAP + RECURSIVE DFS | time: O(n), space: O(n)
        # stores {value, index} for inorder list
        mapToIndex = {val: idx for idx, val in enumerate(inorder)}
        self.preorderIndex = 0  # tracks next preorder value

        def dfs(left, right):
            if left > right:
                return None
            
            # get root value from preorder at current index
            rootValue = preorder[self.preorderIndex]
            self.preorderIndex += 1

            # create node w root value
            root = TreeNode(rootValue)

            # look up inorder index of value
            mid = mapToIndex[rootValue]

            # search left and right
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            
            return root
        
        return dfs(0, len(inorder) - 1)


        ## RECRUSIVE DFS | time: O(n^2), space: O(n)
        # preorder = parent before child, tells first node
        # inorder = left to right, tells left/right subtree
        if not preorder or not inorder:
            return None

        # preorder[0] is always root
        root = TreeNode(preorder[0])

        # find position in inorder, divides into left/right subtree
        mid = inorder.index(preorder[0])        # O(n) each call

        # build left subtree w preorder[1:mid+1] and inorder[0:mid]
        root.left = self.buildTree(preorder[1 : mid+1], inorder[: mid])
        # build right subtree w preorder[mid+1:] and inorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1 :], inorder[mid+1 :])

        return root
        