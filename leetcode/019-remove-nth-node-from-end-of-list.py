# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        now = head
        while now:
            node.append(ListNode(now.val))
            now = now.next

        node.pop(len(node)-n)
        for i in range(0, len(node)-1):
            node[i].next = node[i+1]

        return node[0] if node else None
