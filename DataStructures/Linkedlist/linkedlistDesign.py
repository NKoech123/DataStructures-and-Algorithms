class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self,index):
        if index<self.size or index<0:
            return
        
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val
        
    def addAtIndex(self,index,val):
        
        if index<0 or index>self.size:
            return
        
        to_add=Node(val)
        curr=self.head

        if index==0:  #takes care of when index=0 since our loop doesn't do that
            to_add.next=curr
            self.head=to_add
        for _ in range(index-1):
            curr=curr.next
        to_add.next=curr.next
        curr.next=to_add
        self.size+=1
    
    def addAtHead(self,val):
        self.addAtIndex(0,val)
         
    def addAtTail(self,val):
        self.addAtIndex(self.size,val)
        
    def deleteAtIndex(self,index):
        
        if index<0 or index>=self.size:
            return 
        
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
            
        curr.next=curr.next.next
        self.size-=1
        
      
      
      

#create Nodes        
first=Node(5)
sec=Node(7)
third=Node(9)
tail=Node(11)
ll=Linkedlist()


#linking the nodes and increament size of ll
ll.head=first
ll.size+=1

first.next=sec
ll.size+=1

sec.next=third
ll.size+=1

third.next=tail
ll.size+=1

#param=ll.get(2) #get a value
'''
ll.deleteAtIndex(2)
'''

