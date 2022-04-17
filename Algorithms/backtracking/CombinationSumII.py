class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res=[]
        
        def dfs_backtracking(pos, comb, total):
            
            if total == target:
                res.append(comb.copy())
                
            if total > target or pos>len(candidates):
                return 
            
            prev = -1
            
            for i in range(pos,len(candidates)):
                
                if candidates[i] == prev:
                    continue
                
                comb.append(candidates[i])

                dfs_backtracking(i+1, comb, total+ candidates[i])

                comb.pop()
                
                prev = candidates[i]
                
        dfs_backtracking(0, [], 0)
        
        return res
