# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        pre-order: root->left->right
        
        1
       n   2
         3   n
        stack= [root]
        stack= [r,l]  #order of appending to stack
        stack.pop(0)  #remove top node on stack
        
        stack=[]
        output=[1,2]
        root=[2]
        
        Time complexity:  0(N)
        Space complexity  0(N)  -create of extra space 'output'
        '''
        #base case
        if root is None: return []
        
        stack, output= [root] , [ ]
        while stack:
            root=stack.pop()    
            output.append(root.val)
            
            #check right child. Based on pre-order
            if root.right:
                stack.append(root.right)

            #check left child. Based on pre-order
            if root.left:
                stack.append(root.left)
                
        return output
                
            
        
        
