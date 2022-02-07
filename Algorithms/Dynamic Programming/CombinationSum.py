class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Decision tree-> backtracking DFS
        if remain==0: done!
        if remain < 0 exceeded target. Abandon
        then dfs
        
        '''
        results=[]
        
        def backtrack(remain, comb, start):
            if remain==0:
                results.append(list(comb))
                return
            elif remain<0:
                return
            
            for i in range(start, len(candidates)):
                #add number into the combination
                comb.append(candidates[i])
                #give the current number another chance
                backtrack(remain-candidates[i], comb, i)
                #backtrack, remove the number from the combination
                comb.pop()
                
        backtrack(target, [], 0)
        
        return results
