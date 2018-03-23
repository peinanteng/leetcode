class TrieNode:
    def __init__(self):
        self.childs = [None] * 26
        self.leaf = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        if len(word) == 0:
            return
        node = self.root
        for letter in word:
            k = ord(letter) - ord('a')
            if node.childs[k] is None:
                new_node = TrieNode()
                node.childs[k] = new_node
            node = node.childs[k]
        node.leaf = True
                
    def search(self, word):
        if len(word) == 0:
            return False
        return self.searchHelp(word, self.root, 0)
        
    def searchHelp(self, word, node, i):
        if len(word) == i:
            return node.leaf
        if word[i] == '.':
            for j in range(26):
                if node.childs[j]:
                    if self.searchHelp(word, node.childs[j], i + 1):
                        return True
        j = ord(word[i]) - ord('a') 
        if node.childs[j]:
            if self.searchHelp(word, node.childs[j], i + 1):
                    return True
        return False
            
                
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)
        


