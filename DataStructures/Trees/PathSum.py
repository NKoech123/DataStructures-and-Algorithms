# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        '''recursive solution'''
            
        #base case
        if root is None: 
            return False
        
        #target_sum after subtracting the root's value
        targetSum-=root.val
        
        # confirm leaf has been reached
        if not root.left and not root.right:   
            return targetSum==0
          
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
      
        
         
        
        
