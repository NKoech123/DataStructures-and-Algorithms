'''
Leetcode No. 328
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None: return None
        odd=head
        even=head.next
        evenHead=head.next
        
        while (even!=None and even.next!=None):
            #Putting odd to the odd list
            odd.next=odd.next.next
            
            #Putting even to the even list
            even.next=even.next.next
     
            #Move pointer to the next odd/even
            odd=odd.next
            even=even.next     
        odd.next=evenHead
        
        return head