#LeetCode No.234



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        LL before reverse == LL after reversing
        '''
        count=0
        List=[]
        curr=head
        while curr:
            count+=1
            List.append(curr.val)
            curr=curr.next

        p1=0     #first pointer at index 0
        p2=count-1  # second pointer at right most index
        output=True #Assume it's a palindrome

        while p1<=p2:
            if List[p1]==List[p2]:
                pass     # Always a palindrome as stated on outpute before the loop
            else:
                output=False
                break
            p1+=1
            p2-=1
        return output
