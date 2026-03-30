# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        #reverse the second half
        #two pointer traverse
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        prev = None
        part2 = cur
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        part1 = head
        part2 = prev
        while part2:
            temp = part2.next
            part2.next = part1.next
            part1.next = part2
            part1 = part2.next
            part2 = temp
       
        
            


            


       