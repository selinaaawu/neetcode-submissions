class TrieNode:
    def __init__(self):
        self.children = {}          # map {letter : TrieNode}
        self.endOfWord = False      # marks completion of word


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # if char not in tree -> create trienode for char
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # end of word
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # if char not in tree -> word does not exist
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # shows complete word
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            # if char not in tree -> prefix does not exist
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        