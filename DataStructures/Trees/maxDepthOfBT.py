# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import TreeClass

class Solution:
    def maxDepth(self, root) -> int:
        
        if root is None: 
            return 0
           
        left_node=self.maxDepth(root.left)
        right_node=self.maxDepth(root.right)

        return max(left_node,right_node)+1
