class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        candidates = [2,3,6,7], target = 7
        
        res= []

        '''
        
        res=[]
        
        def dfs_backtracking(i, comb, total):
            
            if total == target:
                res.append(comb.copy())
                return 
            
            if total> target:
                return 
         
            
            for i in range(i,len(candidates)):
                
                comb.append(candidates[i])
                
                dfs_backtracking(i, comb, total+candidates[i])
                
                comb.pop()
                

            
        dfs_backtracking(0, [], 0)
        
        return res
