
from collections import deque
class Solution:
    def levelOrder_BFS(self, root: Optional[TreeNode]) -> List[List[int]]:
      
        levels,level=[],0
        
        if not root:
            return levels
        
        Q=deque([root])
        
        while Q:
            
            levels.append([])
            
            for _ in range(len(Q)):
                
                node = Q.popleft()
                
                levels[level].append(node.val)
                
                if node.left:
                    Q.append(node.left)
                    
                if node.right:
                    Q.append(node.right)
                    
            level+=1
            
        return levels
      
      def level_order_DFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        
          levels ,level = [], 0

          if not root: return levels

          def helper(node , level):

              levels.append([]) if len(levels)==level else levels

              levels[level].append(node.val)

              if node.left:
                  helper(node.left ,level+1)

              if node.right:
                  helper(node.right,level+1)

          helper(root , 0)

          return levels
