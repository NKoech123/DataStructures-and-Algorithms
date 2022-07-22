# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        1. Problem Formulation
            -BST features
                -left nodes <<< parent nodes
                -right nodes >>> parents nodes
                -all above have to be valid
                
            - empty trees are BSTs
        2. Thought process
           - check base case cause about empty_tree==BST
           -Let's create stack of [(root,lower_bound,upper_bound)]
                 -lower_bound represents -math.inf 
                    -for left-tree upper_bound= root.val, lower_bound=-math.inf
                 
                 -upper_bound (math.inf)
                     -for right-tree the upper_bound= math.Inf 
                      lower_bound = root.val
        
        
        
        3. Time Complexity analysis
           Time: O(N)- we visit each node excatly once
           Space: O(N)- due to the stack we use
        
       
          
        (root,lower_bound,upper_bound)
        
        '''
        stack = [(root,-math.inf,math.inf)]
        while stack:
            root,lower,upper = stack.pop()
            if not root:
                continue
                
            val = root.val
            if val<=lower or val>= upper: #sanity check
                return False

            stack.append((root.right, val , upper))
                
            stack.append((root.left, lower , val))
            
        return True
    def isValidBST_recursive(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower=-math.inf,upper=math.inf):
            #empty trees are valid BSTs
            if not root:
                return True
            
            if node.val<=lower or node.val>=upper:
                return False
            return (validate(node.right , node.val , upper) and
            validate(node.left , lower, node.val))
        
