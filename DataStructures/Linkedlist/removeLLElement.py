
#Leetcode No. 203

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        '''
        base case
        '''
        sentinel=ListNode(0,next=head)
    
        
        prev,curr=sentinel,head
        
        while curr:
            if curr.val==val:
                prev.next=curr.next  #deleting action
            else:
                prev=curr
            curr=curr.next
            
        return sentinel.next    #sentinel will always point to the LL head
