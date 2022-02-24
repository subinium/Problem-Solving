# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        now = head
        while now:
            l += 1
            now = now.next

        for i in range(l//2):
            head = head.next

        return head
