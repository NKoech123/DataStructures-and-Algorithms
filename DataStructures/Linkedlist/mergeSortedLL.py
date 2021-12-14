# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        
        list1 = 1 -> 2 -> 4  
        list2 = 1 -> 3 -> 4
        
        sentinel Linkedlist = [1000,1,1,2,3,4]
        
        '''
        sentinel=ListNode(1000)
        prev=sentinel
        
        #Loop through both lists
        while list1 and list2:
            
            #traverse list1 and check if it's smaller
            if list1.val<=list2.val:
                prev.next=list1
                list1=list1.next
                
            
            else:   #otherwise next node is list2 and traverse
                prev.next=list2
                list2=list2.next
                
            prev=prev.next
       
        if list1 is not None:
            prev.next=list1 
        else:
            prev.next=list2
         
        
        return sentinel.next
        