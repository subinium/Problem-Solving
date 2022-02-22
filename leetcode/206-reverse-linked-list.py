# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        now = head
        while now:
            lst.append(ListNode(now.val))
            now = now.next

        lst.reverse()
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]

        return lst[0] if lst else None
