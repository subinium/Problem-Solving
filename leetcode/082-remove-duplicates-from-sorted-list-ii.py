# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        d = defaultdict(lambda: 0)
        while head:
            val = head.val
            vals.append(val)
            d[val] += 1
            head = head.next

        vals = [ListNode(val) for val in vals if d[val] == 1]
        for i in range(len(vals)-1):
            vals[i].next = vals[i+1]

        return vals[0] if vals else None
