# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        sumList = ListNode()
        head = sumList
        remainder = 0
        while p1 and p2:
            total = (p1.val + p2.val + remainder) 
            sumList.next = ListNode(total % 10)
            remainder = total // 10
            p1 = p1.next
            p2 = p2.next
            sumList = sumList.next
        if p1:
            while p1:
                total = p1.val + remainder
                sumList.next = ListNode(total % 10)
                remainder = total // 10
                p1 = p1.next
                sumList = sumList.next
        if p2:
            while p2:
                total = p2.val + remainder
                sumList.next = ListNode(total % 10)
                remainder = total // 10
                p2 = p2.next
                sumList = sumList.next
        if remainder > 0:
            sumList.next = ListNode(remainder)

        return head.next
