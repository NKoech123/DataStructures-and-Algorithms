# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        -find middle of LL. fast and slow pointer
              (even,odd LL)
        -reverse the last half of the LL
        
        -reorder(merge with alternating values): 
               -tmp.next = p2
        
        
        [1 ->   2  ->   3    ->4  ]
               slow          fast          
        
     
          
         [1 ->   2     -> None  <-   3         <-4  ]
         
                 slow                           prev    second
                 
        [1->2->None]  [4->3->None]
           c1             c2
         
         1->4->2->3
               p
        '''    
        
        fast,slow = head.next, head
        
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
        second = slow.next
        slow.next = None
        prev=slow.next
        
        while second:
            temp = second.next
            second.next = prev
            
            prev = second
            second= temp
            
            
        first,second = head, prev
        
        while second:
            temp1, temp2=first.next,  second.next
            
            first.next = second
            second.next = temp1
            
            first,second = temp1, temp2
