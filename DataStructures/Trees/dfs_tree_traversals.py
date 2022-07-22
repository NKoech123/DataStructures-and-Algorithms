'''
This covers all iterative and recursive dfs tree traversals : preorder , inorder , postorder

preorder traversal follows the order [root,left,right]
inorder traversal follows the order [left,root,right]
preorder traversal follows the order [left,right,root]


'''
from collections import deque
class TreeNode:

    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right

    
def iterative_preorder(root):
    
    if not root: 
        return

    stack , res =[] ,[]
    stack.append(root)

    while stack:

        node=stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


def recursive_preorder(root):
    
    res=[]
    
    if root:

       res.append(root.val)

       recursive_preorder(root.left)

       recursive_preorder(root.right)

    return res



def iterative_inorder(root):
    
    res=[]
    stack=deque([])
    curr=root
    while stack or curr:
        
        if curr: #if curr node exists, push it to the stack and move to left child
            stack.append(curr)
            curr=curr.left

        else: #otherwise if the curr is None, then pop top stack and maybe print it
            curr=stack.pop()
            res.append(curr)
            curr=curr.right
         

def recursive_inorder(root):
    
    res=[]
    
    if root:
        #first , recur on the left child
        recursive_inorder(root.left)
        #then append/print the data of the node
        res.append(root.val)
        #now recur on right child
        recursive_inorder(root.right)

    return res


def iterative_postorder(root):

    if not root: return 
   
    #create empty stack and push root node
    stack=deque([root])
    #create another result stack to store postorder traversal
    res=deque([])

    while stack:
        curr=stack.pop()
        res.append(curr.val)

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    #print postorder traversal
    res_val=[]
    while res:
        res_value=res.pop()
        res_val.append(res_value)

    return res_val

def recursive_postorder(root):
    
    res=[]

    if root:
        #first recur on the left child
        recursive_postorder(root.left)
        #then recur on the right child
        recursive_postorder(root.right)
        #then append/print the data of the node
        res.append(root.val)

    return res


#Driver program to test above
 
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)



   
    

    

