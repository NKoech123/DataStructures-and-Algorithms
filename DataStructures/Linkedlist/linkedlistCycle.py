class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    
        
    def hasCycle(self, head) -> bool:
        nodes_seen = set()
        while head:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
        

#Driver Code

#First create Node instances
a=Node(3)
b=Node(2)
c=Node(0)
d=Node(-4)


ll=Linkedlist()
#Define head and link the nodes
ll.head=a
a.next=b 
b.next=c
c.next=d
d.next=b #tail is linked to pos=1. 


#run the hasCycle method to check if the LL created above is a cycle
ll.hasCycle(a)