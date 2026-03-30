# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        current = newHead
        cur1 = list1
        cur2 = list2
        if not cur1:
            return cur2
        elif not cur2:
            return cur1
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                current.next = cur1
                current = current.next
                cur1 = cur1.next    
            else:
                current.next = cur2
                current = current.next
                cur2 = cur2.next
        if cur1:
            current.next = cur1
        elif cur2:
            current.next = cur2
        return newHead.next   