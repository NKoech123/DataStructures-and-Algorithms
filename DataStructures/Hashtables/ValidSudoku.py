class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
        input-> board[r][c]
        r: 0-8
        c: 0-8
        boxes: 0-8 
        
         box_index= [ box_index=0- r:0-2 and c:0-2]
                                0  r=1 
        '''
        #Function to find index of the boxes
        def find_boxIndex(r,c):
            return (r // 3)  + 3*(c // 3)
        #create hash sets for rows , cols and boxes
        size=9
        rows= [set() for _  in range(size)]
        cols= [set() for _  in range(size)]
        boxes= [set() for _  in range(size)]
        
        for r in range(size):
            for c in range(size):
                
                #initialize value in a sudoku cell
                value=board[r][c]
                
                if value==".":
                    continue
                '''
                 check cols,rows,boxes if value exists, if not pass, if
                 value exists, add to the set

                 '''   
                #check boxes
                boxIndex=find_boxIndex(r,c)
                if value in boxes[boxIndex]:
                    return False
                boxes[boxIndex].add(value)
                
                #check rows
                if value in rows[r]:
                    return False
                rows[r].add(value)
                
                #check cols
                if value in cols[c]:
                    return False
                cols[c].add(value)
                
                
        return True
                
               