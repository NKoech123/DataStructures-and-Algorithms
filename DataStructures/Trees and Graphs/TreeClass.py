class TreeNode:
    '''Node stores its value and next left,right pointers'''
    def __init__ (self,val,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=None #pointe to parent node in tree

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0  #optional but will implement it

    def insert(self,val):
        if self.root==None:
            self.root=TreeNode(val)
            self.size+=1
        else:
            self._insert(val,self.root)
    def _insert(self,val,cur_node):
        """check if value qualifies to be added on left/right tree"""
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left=TreeNode(val)
            else:
                self._insert(val,cur_node.left)
        
        elif  val > cur_node.val:
            if cur_node.right==None:
                cur_node.right=TreeNode(val)
            else:
                self._insert(val,cur_node.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node:
            self._print_tree(cur_node.left)
            print(cur_node.val)
            self._print_tree(cur_node.right)

    def height(self):
        if self.root:
            return self._height(self.root,0)
        else:
            return 0
    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self.height(cur_node,cur_height+1)
        right_height=self.height(cur_node,cur_height+1)
        return max(left_height,right_height)
    
    def search (self,value):
        if self.root:
            return self._search(val,self.root)
        else:
            return False
    def _search (self,val,cur_node):
        if val==cur_node.val:
            return True
        elif  val<cur_node and cur_node.left!=None:
             return self._search(val,cur_node.left)
        elif val>cur_node and cur_node.right!=None:
            return self._search(val,cur_node.right)
        return False
            


tree=BinarySearchTree()


tree.insert(1)
tree.insert(0)
tree.insert(3)
tree.print_tree()