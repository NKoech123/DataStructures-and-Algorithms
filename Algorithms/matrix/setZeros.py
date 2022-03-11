class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited=[]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                
                if matrix[r][c]==0 :
                    visited.append((r,c))
                    
        return self.setter(matrix,visited)

    def setter(self ,matrix, visited):
        
        for row,col in visited:
            
            for r in range(len(matrix)): 
                    if matrix[r][col]!=0:
                        matrix[r][col]=0
                    
            for c in range(len(matrix[0])): #replace at constant row
                   if matrix[row][c]!=0:
                        matrix[row][c]=0 
        
        return matrix
