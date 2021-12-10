'''
Approach: Floyd's Cycle
Hare and the tortoise (Space compexity 0(1) and Time Complexity 0(n))

'''
class Solution(object):
    def getIntersect(self,head):
     
        fast=head
        slow=head
        '''
         The goal is to have the fast pointer loop around a cycle and meet            the slow pointer or reach null at the end of the linkedlist
        '''
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return slow
        return None 
    
    
    def detectCycle(self, head):
        if head is None:
            return None
        '''
        Get the intersection node
        '''
        intersect=self.getIntersect(head)
        if intersect is None:
            return None
        '''
        Two pointers(one from head and other from intersection node)                 traversing at same speed.Goal is to identify where they meet.
        '''
  
        ptr1=head
        ptr2=intersect
        while ptr1!=ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next
            
        return ptr1