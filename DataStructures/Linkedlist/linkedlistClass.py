class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Linkedlist(object):

    def __init__(self):
        self.head = None
        self.size = 0
    
    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index, val):

        if index > self.size:
            return
        
        current = self.head
        newNode = ListNode(val)
                
        if index == 0:
            newNode.next = current
            self.head = newNode
        else:                        
            for i in range(index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode    
    
        self.size += 1

    def printll(self):
        print_val=self.head
        while print_val:
            print(print_val.val)
            print_val=print_val.next

        
    def remoteNthFromEnd(self, head, n):
        p1=p2=head
        for _ in range(n):
            p2=p2.next  
        if not p2:
            return head.next
        while p2.next:
            p1=p1.next
            p2=p2.next
        #p1.next=p1.next.next
        p1.next=p1.next.next
        
        return head
        

   
"""Driver Code"""
if __name__ == '__main__':
    ll=Linkedlist()
    #ll.addAtIndex(index,val)
    ll.addAtIndex(0, 1)
    ll.addAtIndex(1, 2)
    ll.addAtIndex(2, 3)
    ll.addAtIndex(3, 4)
    ll.addAtIndex(4, 5)

  
  
    #Before removing Nth Element from the End
    ll.printll()
    
    #After removing Nth Element from the End
    ll.remoteNthFromEnd(ll.head, 2)
    ll.printll()

 
 






