# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        '''
        preorder = [20,15,7]  root,left,right
        inorder = [9,3,15,20,7]   left,root,right
        left_tree=[]
        right_tree=[15,20,7]
        
        '''
        if not preorder or not inorder:
            return None
        
        root_val = preorder.pop(0)
        left_tree = inorder[0:inorder.index(root_val)]
        right_tree = inorder[inorder.index(root_val)+1:]
        
        
        root = TreeNode(root_val)
        root.left = self.buildTree (preorder, left_tree)
        root.right = self.buildTree(preorder, right_tree)
        
        return root
    


class More_Optimal_Solution:
    '''
    Use of hashmap to provive 0(1) time when indexing inorder
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        inorder_cache = {} 
        for idx,val in enumerate(inorder):
            inorder_cache[val]=idx
        
        def helper (preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root_val = preorder.pop(0)
            left_tree= inorder[0:inorder_cache[root_val]]
            right_tree=inorder[inorder_cache[root_val] + 1:]

        
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder,left_tree)
            root.right =self.buildTree(preorder,right_tree)

            return root
        return helper(preorder, inorder)
