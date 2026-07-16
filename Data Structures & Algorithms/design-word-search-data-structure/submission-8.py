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
        # recurisve 
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                char = word[i]
                # if wildcard -> go through every child
                if char == ".":
                    print("WILDCARD:", char)
                    for child in curr.children.values():
                        # try EVERY possible child
                        # skip comparison for "." character
                        if dfs(i + 1, child):
                            return True
                    # no matching child found
                    return False
                # if regular character not exist -> word not exist
                elif char not in curr.children:
                    return False
                # otherwise -> shift pointer to node
                curr = curr.children[char]
            # actual word
            return curr.endOfWord

        return dfs(0, self.root)

        
