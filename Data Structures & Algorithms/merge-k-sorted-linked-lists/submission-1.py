# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #create a function to sort 2 lists
        #go through the lists and sort 2 to begin then sort the next one


        def merge2Lists(root1,root2):
            list1 = root1
            list2 = root2
            res = ListNode(0)
            head = res
            while list1 or list2:
                if list1 and list2:
                    if list1.val <= list2.val:
                        res.next = ListNode(list1.val)
                        list1 = list1.next
                    else:
                        res.next = ListNode(list2.val)
                        list2 = list2.next
                elif list1:
                    res.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    res.next = ListNode(list2.val)
                    list2 = list2.next

                res = res.next
            return head.next


        if len(lists) < 1:
            return None
        elif len(lists) < 2:
            return lists[0]
        for i in range(1,len(lists)):
            lists[i] = merge2Lists(lists[i - 1],lists[i])
        return lists[-1]

