# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  '''
  isSubtree- recursively digs deeper into root tree to check if there exists a root_val in which root.val==subRoot.val
             if such root exists, call the isMach meth below:
  isMatch meth- recursively compares nodes in root and subroot
  
  '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isMatch(root,subRoot): #let's go defin this func
                return True
        
        return (self.isSubtree(root.left,subRoot) or
               self.isSubtree(root.right,subRoot))

    def isMatch(self, root, sub_root):
        if not root and not sub_root:
            return True
        
        if not root:
            return False
        
        if not sub_root:
            return False
        
        if root.val!=sub_root.val:
            return False
    
        
        return (self.isMatch(root.left, sub_root.left) 
                and self.isMatch(root.right, sub_root.right))
    
        
