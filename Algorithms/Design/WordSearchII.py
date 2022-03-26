'''LeetCode 212'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
        
    def addWord(self,word):
        currNode=self
        
        for char in word:
            if char not in currNode.children:
                currNode.children[char] = TrieNode()
            currNode = currNode.children[char]
        currNode.isWord=True
         


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #let's add all words to our Trie data structure
        root=TrieNode()
        for word in words:
            root.addWord(word)
            
        COLS,ROWS = len(board[0]),len(board)
        res,visit=set(),set()
        
        
        def dfs(r,c,node,word):
            
            if (r<0 or c<0 or r==ROWS or c==COLS or 
                (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            
            node=node.children[board[r][c]]
            word+=board[r][c]
            
            if node.isWord:
                res.add(word)
                
            dfs(r-1,c,node,word)
            dfs(r+1,c,node,word)
            dfs(r,c-1,node,word)
            dfs(r,c+1,node,word)
            
            visit.remove((r,c))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
        return list(res)
        
        
