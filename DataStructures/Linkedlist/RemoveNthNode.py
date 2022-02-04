# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        -create dummyhead,then start fast and slow pointers at dummyhead
        -run the fast pointer n steps head, then run both pointers
        until fast pointer is at the tail.
        -then remove the nth node(the node next to slow node)
        -Time 0(L) L is length of the LL
        -Space 0(1), we only used constant extra space
     
        '''
        
        dummyhead=ListNode(-1,head)
        
        fast=slow=dummyhead
        
        for _ in range(n):
            fast=fast.next
            
        if fast is None: #means the nth node is not in LL
            return head 
        
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        
        
        return dummyhead.next
