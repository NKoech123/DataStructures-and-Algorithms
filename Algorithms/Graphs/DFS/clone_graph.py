"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node, clone_map):
            if clone_map is None: 
                clone_map={}

            if not node: return node

            if node in clone_map:
                return clone_map[node]

            cloned_node=Node(node.val,[])
            clone_map[node]=cloned_node


            if node.neighbors:
                cloned_node.neighbors=[dfs(n, clone_map) for n in node.neighbors]

            return cloned_node
        return dfs(node,{})
    
