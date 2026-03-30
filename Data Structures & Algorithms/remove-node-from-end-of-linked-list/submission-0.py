# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        target = count - n
        new = head
        if n == count:
            return head.next
        for i in range(0,target - 1):
            new = new.next
        if new.next.next:
            new.next = new.next.next
        else:
            new.next = None
        return head 





        
        

        


        