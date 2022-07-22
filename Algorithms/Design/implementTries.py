'''
LeetCode 208
'''
class TrieNode:
    def __init__(self):
        #key is 'char' and value is node
        self.children={}
        self.endOfword=False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.endOfword=True
       
    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return curr.endOfword
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
