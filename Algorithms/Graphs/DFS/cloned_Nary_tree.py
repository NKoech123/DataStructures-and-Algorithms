#similar to clone graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        
        def dfs(node,deep_copy):
            
            if not deep_copy:
                deep_copy={}
            
            if not root:
                return root
            
            if node in deep_copy:
                return deep_copy[node]
            
            cloned_node=Node(node.val,[])
            
            deep_copy[node]=cloned_node
            
            if node.children:
                cloned_node.children= [dfs(n,deep_copy) for n in node.children]
            
            return cloned_node
        return dfs(root,{})
        
        
        
