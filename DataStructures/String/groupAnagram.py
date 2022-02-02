class Solution:
      '''
      make count=[0]*26 represent each string,
      the map the count to their corresponding
      string values in the hashmap

      '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap=collections.defaultdict(list)
        
        for s in strs:
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            hashmap[tuple(count)].append(s)
            
        return hashmap.values()
                
