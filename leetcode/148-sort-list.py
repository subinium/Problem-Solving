# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = []
        while head:
            node.append(ListNode(head.val))
            head = head.next

        node = sorted(node, key=lambda x: x.val)
        for i in range(len(node)-1):
            node[i].next = node[i+1]

        return node[0]
