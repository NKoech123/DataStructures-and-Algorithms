"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    
    def cloneGraph_dfs(self, node) -> 'Node':
        
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
    

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
 
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        -We create our first clone_node and make a reference in hashtable,
        then add the node of the cloned node to the Queue.
        -We go check the neighbors, clone them and make an association with 
        the "parent" node.
        
        '''

        if not node:
            return node
        
        visited = {}
        Q = deque([node])
        visited[node] = Node(node.val, []) #initiate to populate the hashmap
        
        while Q:
            
            n = Q.popleft()
            
            for nei in n.neighbors:
                
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    Q.append(nei)
                
                visited[n].neighbors.append(visited[nei])
                
        return visited[node]