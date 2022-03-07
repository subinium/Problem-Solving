# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while list1:
            l.append(list1.val)
            list1 = list1.next
        while list2:
            l.append(list2.val)
            list2 = list2.next

        l.sort()
        ln = [ListNode(n) for n in l]
        for i in range(len(ln)-1):
            ln[i].next = ln[i+1]

        return ln[0] if ln else None
