# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        need = count - n
        if need == 0:
            return head.next
        prev = ListNode(0)
        prev.next = head
        cur = prev

        for i in range(0,need):
            cur = cur.next
        cur.next = cur.next.next
        

        return head
            

        