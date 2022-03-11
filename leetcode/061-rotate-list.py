# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        vals = deque()
        while head:
            vals.append(ListNode(head.val))
            head = head.next
        l = len(vals)
        k %= l
        vals.rotate(k)
        for i in range(l-1):
            vals[i].next = vals[i+1]
        return vals[0]
