# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import TreeClass

class Solution:
    def recursive_maxDepth(self, root) -> int:
        
        if root is None: 
            return 0
           
        left_node=self.maxDepth(root.left)
        right_node=self.maxDepth(root.right)

        return max(left_node,right_node)+1
    

    def iterative_maxDepth(self, root: Optional[TreeNode]) -> int:
        
    
        stack,depth=[],0
        
        if not root:
            return depth
        else:
            stack.append((1,root))
        
        while stack!=[]:
            
            cur_depth,root = stack.pop()
            
            depth = max(depth,cur_depth)
            
            if root.left:
                stack.append((cur_depth+1,root.left))
                
            if root.right:
                stack.append((cur_depth+1,root.right))
                
        return depth
        
