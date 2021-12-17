
#Leetcode 708
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode      #make head point to tail
            return newNode
 
        prev, curr = head, head.next

        while True:
            #Case 1.
            if prev.val <= insertVal <= curr.val:
                 prev.next = Node(insertVal, curr)
                 return head
            #Case 2
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    prev.next = Node(insertVal, curr)
                    return head

            prev, curr = curr, curr.next
            if prev == head:
                break
        #Case 3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head