class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        
        Encode:  s = ["Hello", "World"]
        """
        res= ""
        for s in strs:
            
            res+= str(len(s)) + "#" + s
            
        return res
        
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        
         Decode:  "5# Hello 5#World"
        """
        res, i= [], 0
        
        while i < len(s):
            
            j=i
            
            while s[j] != "#":
                j+=1
                
            length = int(s[i:j])
            
            res.append(s[j+1:j+1+length])
            
            i=j + length + 1
            
        return res
