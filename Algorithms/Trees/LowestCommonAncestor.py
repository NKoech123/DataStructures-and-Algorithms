# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        BST definition:
        left_tree smaller than parent and right_tree ....
        
        p_val>parent_val and q_val>parent_val: then node=node.right
        p_val<parent_val and q_val<parent_val: then node=node.left
        otherwise:
             we have found the ancestor, so return the node
        
        Time: O(log N)-for BST, but O(N)-spindly(worst case)
        Space: O(1)
        '''
        
        while root:
            
            parent_val=root.val
            
            if q.val > parent_val and p.val > parent_val:
                root=root.right
                
            elif q.val < parent_val and p.val < parent_val:
                root=root.left

            else:
                return root
       
