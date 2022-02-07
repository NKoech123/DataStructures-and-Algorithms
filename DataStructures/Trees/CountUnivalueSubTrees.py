# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        if root is None: return 0
        self.count=0
        self.is_uni(root)
        return self.count
        
    def is_uni(self,node):
        
        #base case- node has no children
        if node.right is None and node.left is None:
            
            self.count+=1 #found univalue subtree-increment
            
            return True
        is_uni=True


        if node.left is not None:
            is_uni=self.is_uni(node.left) and is_uni and node.left.val==node.val

        if node.right is not None:
            is_uni=self.is_uni(node.right) and is_uni and node.right.val==node.val

        self.count+=is_uni
        
        return is_uni
        
