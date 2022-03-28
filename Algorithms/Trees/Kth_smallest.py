# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        find smallest val. This val will be on the left most-value(according
        to the definition of BST) 
              -then return (val-1)+k
        '''
        def helper(root,k):
            
            stack =[root]
            val=None

            while stack:
                node = stack.pop(0)

                if node.left is None:
                    return node.val
                   
                stack.append(node.left)
        val=helper(root,k)-1
        return val + k
