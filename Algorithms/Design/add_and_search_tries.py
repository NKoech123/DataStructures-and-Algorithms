class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfword=False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        #start with the empty TrieNode
        currNode=self.root
        
        for c in word:
            
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            currNode=currNode.children[c]
            
        currNode.endOfword=True
        
          
    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            currNode = root
            
            for i in range(j,len(word)):
                c = word[i]
                
                if c==".":
                    for child in currNode.children.values():
                        
                        if dfs(i+1,child):
                            return True
                    return False
                    
                    
                else:
                    if c not in currNode.children:
                        return False
                    currNode=currNode.children[c]
            return currNode.endOfword
            
        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
