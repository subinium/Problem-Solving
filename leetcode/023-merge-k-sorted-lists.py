# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val = []
        for head in lists:
            while head:
                val.append(ListNode(head.val))
                head = head.next
        val.sort(key=lambda x: x.val)
        for i in range(len(val)-1):
            val[i].next = val[i+1]
        return val[0] if val else None
