#LeetCode 833
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        matches = defaultdict(list)  # indices: sources
        
        for i in range(len(indices)):
            if s[indices[i]:].startswith(sources[i]):
                matches [indices[i]] = (sources[i], targets[i])
            
    
        i=0
        new_str=""
        while i < len(s):
            if i in matches:
                src,targz = matches.get(i)
                new_str += targz
                i+=len(src)
                        
            else:
                new_str+=s[i]
                i+=1
                
        return new_str
                
