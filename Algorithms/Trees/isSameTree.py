# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        cases:
        p,q=[],[]            both empty
        
        p,q=[1,2],[1,2,3]    either one is None
        
        p,q=[1,2],[1,2]      classic case (determined at later stage/end)
        
        p,q=[1,2],[1,1]      if p.val!=q.val 
        
        '''
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val :
            return False
        
        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
