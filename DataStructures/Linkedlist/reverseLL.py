class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        
        '''
        if head is None:
            return head
        
        prev,curr=None,head
        
        while curr:
            
            nxt=curr.next #store node nxt
            
            curr.next=prev #actual reversing happening
            
            #move prev and curr one step forward
            prev=curr
            curr=nxt
             
        return prev