'''
This covers all bfs tree traversals (level order traversals)




'''
from collections import queue
class TreeNode:

    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

def bfs(root):
    pass

    
#Driver program to test above
 
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)