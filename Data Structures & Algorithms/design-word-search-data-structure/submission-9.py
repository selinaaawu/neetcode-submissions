class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        # DFS | time: O(length string), space: O(total TrieNode + length string) 
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                char = word[i]
                # if wildcard -> go through every child
                if char == ".":
                    for child in curr.children.values():
                        # try EVERY possible child
                        # skip comparison for "." character
                        if dfs(i + 1, child):
                            return True
                    # no valid child path
                    return False
                else:
                    # if regular character not exist -> word not exist
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            # current node is end of word
            return curr.endOfWord

        return dfs(0, self.root)

        
