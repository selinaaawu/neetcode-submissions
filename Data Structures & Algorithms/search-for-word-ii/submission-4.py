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
        ## TRIE & HASH SET
        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()

        root = TrieNode()
        for i, word in enumerate(words):
            root.addWord(word, i)

        def dfs(r, c, node, word):
            # out of bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS: return
            # board[r][c] already visited
            if (r, c) in visit: return
            # board char does not match trie chars
            if board[r][c] not in node.children: return 

            visit.add((r, c))                   # mark cell as visited
            node = node.children[board[r][c]]   # iterate to children
            word += board[r][c]                 # add to word string

            if node.index != -1:                # if end of word, add to result
                result.add(word)
            
            # recurse through all row/col
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))                # restore cell to original
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
            
        return list(result)
        


        ## BRUTE FORCE | time: O(# words * ROWS * COLS * 4^(max word length))
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
                        
        

