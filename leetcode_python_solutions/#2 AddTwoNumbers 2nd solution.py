# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1pointer = l1
        l2pointer = l2
        carry  = 0
        ans = ListNode(0)
        curr = ans

        while l1pointer or l2pointer :
             val1 = l1pointer.val if l1pointer else 0 
             val2 = l2pointer.val if l2pointer else 0 
             sum = carry + val1 + val2
             carry =  sum // 10 
             curr.next  = ListNode(sum % 10)
             curr = curr.next
             if l1pointer :
                l1pointer = l1pointer.next
             if l2pointer :
                l2pointer = l2pointer.next
        
        if(carry > 0) :
            curr.next  = ListNode(carry)
            
        return ans.next
        