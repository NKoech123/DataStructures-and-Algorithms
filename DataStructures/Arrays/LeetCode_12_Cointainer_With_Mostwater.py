
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
        


    def maxArea_anotherSol(self, height: List[int]) -> int:
        '''
        
        [1, 8, 6, 2, 5, 4, 8, 3, 7]
                r
            l
        '''
        
        area, max_area = 0,0
        
        l, r = 0, len(height)-1
        
        while l<r:
            
            area = min(height[l], height[r]) * (r-l)
            max_area = max (max_area, area)
            
            if height[l] <= height[r]:
                l+=1
                
            else:
                r-=1
                
        return max_area
            
