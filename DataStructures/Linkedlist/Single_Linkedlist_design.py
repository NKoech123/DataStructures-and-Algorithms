class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        
        for _ in range(index):            
            current = current.next

        return current.val
    
    def addAtHead(self, val):
   
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        
        if index > self.size:
            return
        
        current = self.head
        newNode = ListNode(val)
                
        if index <= 0:
            newNode.next = current
            self.head = newNode
        else:                        
            for _ in range(index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode    
            
        self.size += 1
        
    def deleteAtIndex(self, index):
       
        if index < 0 or index >= self.size:
            return
        
        current = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next              

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


