# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

       
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        prev = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        right = prev
        left = head
        
        while right:
            temp1 = left.next
            temp2 = right.next
            right.next = temp1
            left.next = right
            left = temp1
            right = temp2

        


            


            