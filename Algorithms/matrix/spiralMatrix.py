#LeetCode 54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result=[]
        rows,columns = len(matrix) , len(matrix[0])
        up,left=0,0
        right=columns-1
        down=rows-1
    
        
        while len(result) < rows*columns:
            
            #traverse from left to right
            for col in range(left,right+1):
                result.append(matrix[up][col])
                
            #traverse downwards
            for row in range(up+1,down+1):
                result.append(matrix[row][right])
                
            #Make sure we are in a different row
            
            if up!=down:
                #traverse from right to left
                for col in range(right-1,left-1,-1):
                    result.append(matrix[down][col])
                    
            #Make sure we are in a different column
            if left!=right:
                #traverse upwards
                for row in range(down-1,up,-1):
                    result.append(matrix[row][left])
                
            left+=1
            right-=1
            up+=1
            down-=1
            
        return result
   
      
