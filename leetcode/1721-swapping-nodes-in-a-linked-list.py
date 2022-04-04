# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        lst = []
        while head:
            lst.append(ListNode(head.val))
            head = head.next
        lst[k-1], lst[-k] = lst[-k], lst[k-1]
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        return lst[0]