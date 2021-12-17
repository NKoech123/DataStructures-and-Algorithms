"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        #creating new weaved list of original and copied nodes
        ptr=head
        
        while ptr:
            
            #Cloned node
            new_node=Node(ptr.val,None,None)
            
            #Insert clones node next to the original node  ptr=A->B
            new_node.next=ptr.next       # A'->B
            ptr.next=new_node            # A->A'
            
            ptr=new_node.next
            
        ptr=head
        
        #linking the random pointers of the new nodes created
        
        while ptr:
            ptr.next.random=ptr.random.next if ptr.random else None
            ptr=ptr.next.next
            
        #Unweave the linked list to get back the original LL and the cloned list
        ptr_old_list=head
        ptr_new_list=head.next
        
        head_new=head.next
        
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
        