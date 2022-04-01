# "Today is Monday greatest"
class Solution:
    
    '''
    def intersperse(e, l):

         res = "".join(i + j for i, j in zip(e, l))

         return  res
    '''

    def findMax(self,s):
        max_string = []
        s=s.split()
        for idx,elem in enumerate(s):
            max_string.append((idx,self.findFreq(elem)))

        idx=max(max_string, key=lambda x:x[1])[0]

        return s[idx]
    
    def findFreq(self, word):
        freq=0
        visited= {char:0 for char in word }

        for char in word:
            if char in visited:
                visited[char]+=1
            
        for count in visited.values():
            if count>1:
                freq+=1
        return freq

s= "Today is Monday greatest"
print(Solution().findMax(s))
