# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)
        
        
    def isMirror(self,root1,root2):
        #base case
        if root1 is None and root2 is None:
            return True
        '''
         -For tree to be symmetric,it behave like it's mirrored,satisying the conditions
         below:
         left tree                right tree=> (copy left tree )       
            2 
            /\
           3   3
          /\   /\
         4  3 3  4 
     
           1. values in left root is equal to values in the right root (root1.val==root2.val)
           2. left tree's left subtree is mirrored image of right tree's right subtree
             code: self.isMirror(root1.left,root2.right)
           3. left tree's right subtree is mirrored image of right tree's left subtree
             code: self.isMirror(root1.right,root2.left)
      
        '''
        if root1 and root2:
            if root1.val==root2.val:
                return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))
        
        return False
    

        
