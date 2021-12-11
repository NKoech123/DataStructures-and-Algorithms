class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two-pointer
        left=right=head
        
        for _ in range(n):
            right=right.next
            
        if right is None:
            return head.next
        while right.next:
            left=left.next
            right=right.next
        left.next=left.next.next
        
        return head