# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return None
        if len(lists) == 0:
            return None


        def merge2(list1,list2):
            cur1 = list1
            cur2 = list2

            tail = ListNode()
            head = tail
            while cur1 and cur2:
                if cur2.val <= cur1.val:
                    tail.next = cur2
                    tail = tail.next
                    cur2 = cur2.next
                else:
                    tail.next = cur1
                    tail = tail.next
                    cur1 = cur1.next
            if cur1:
                tail.next = cur1
            elif cur2:
                tail.next = cur2
            return head.next
                    
                    

            



        for i in range(1,len(lists)):
            lists[i] = merge2(lists[i],lists[i-1])


        return lists[-1]



