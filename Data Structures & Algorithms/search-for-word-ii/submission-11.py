class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1         # index of word in words if exists

    def addWord(self, word, i):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.index = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ## TRIE | time: O(m * n * 4 * 3^(max word length) + sum length all word)
        # trie of all word in words
        root = TrieNode()
        for i, word in enumerate(words):
            root.addWord(word, i)
        
        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            # out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return

            char = board[r][c]
            # board[r][c] already visited or not in trie chars
            if char == "*" or char not in node.children: return

            child = node.children[char]          # iterate to children

            # if end of word, add to result and remove index marking
            if child.index != -1:                
                result.append(words[child.index])
                child.index = -1                 # avoids duplicates
            
            board[r][c] = "*"                   # mark as visited

            # recurse through all neighbors
            dfs(r + 1, c, child)
            dfs(r - 1, c, child)
            dfs(r, c + 1, child)
            dfs(r, c - 1, child)
            
            board[r][c] = char                  # restore to original

            if not child.children:
                del node.children[char]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
            
        return result
        


        ## BRUTE FORCE | time: O(# of words * m * n * 4 * 3^(max word length) - 1)
        # implementation is correct but fails due to inefficiency
        print("brute")
        ROWS, COLS = len(board), len(board[0])
        result = []

        # where r = row, c = col, i = position of word
        def backtrack(r, c, i):
            # entire word found
            if i == len(word): return True                
            # out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return False                
            # already visited or char does not match
            if board[r][c] != word[i]: return False
            
            board[r][c] = "*"       # mark cell as visited
            # check neighbors with i + 1
            match = (backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or 
                     backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1))
            board[r][c] = word[i]   # revert cell to original
            return match
        
        # for each word, check board[r][c] for matching words
        for word in words:
            found = False
            for r in range(ROWS):
                if found: break
                for c in range(COLS):
                    # if board matches first char
                    if board[r][c] == word[0]:
                        # EVERY possible backtrack for first char
                        if backtrack(r, c, 0):
                            result.append(word)
                            found = True
                            break
        
        return result
                        
        

