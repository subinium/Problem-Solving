# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = []
        while head:
            node.append(ListNode(head.val))
            head = head.next

        n = len(node)
        for i in range(1, n, 2):
            node[i-1], node[i] = node[i], node[i-1]
        for i in range(n-1):
            node[i].next = node[i+1]

        return node[0]
