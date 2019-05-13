# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = 0
        val2 = 0
        index  = 0
        l1pointer = l1
        while l1pointer :
            val1 = l1pointer.val * pow(10, index) + val1
            l1pointer = l1pointer.next
            index += 1
        index = 0    
        l2pointer = l2
        while l2pointer :
            val2 = l2pointer.val *  pow(10, index) + val2
            l2pointer = l2pointer.next
            index += 1
        final = str(val1 + val2)
        temp = None
        for i in range(0, len(final)) :
             node = ListNode(final[i])
             node.next= temp
             temp = node
            
        return node
        