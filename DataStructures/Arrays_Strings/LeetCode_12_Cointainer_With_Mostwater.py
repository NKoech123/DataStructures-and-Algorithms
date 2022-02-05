
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
                  i                       j
        Shrinking window:
        check if i<j or otherwise:
           -if i<j : compute area, then i+=1
           -if i>j : compute area, then j-=1
        
        take min([height[i],height[j]]) * (j-i)
        
        Time O(N) -single pass
        Space O(1) -constant space is used
        '''
        i , j = 0 , len(height)-1
        
        max_area , local_area = 0 , 0
        
        while i<j:
            
            if height[i]<=height[j]:
                
                local_area = ( min([height[i],height[j]]) * (j-i) )
                
                max_area = max(max_area,local_area)
                
                i+=1
            
            else:
                
                local_area = ( min([height[i],height[j]]) * (j-i) )
                
                max_area = max(max_area,local_area)
                
                j-=1
                
        return max_area
        
       
            
