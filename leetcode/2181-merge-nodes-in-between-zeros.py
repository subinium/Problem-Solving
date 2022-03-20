# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        val = 0
        while head:
            val += head.val
            if head.val == 0:
                lst.append(ListNode(val))
                val = 0
            head = head.next

        lst = lst[1:]
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]

        return lst[0] if lst else None
