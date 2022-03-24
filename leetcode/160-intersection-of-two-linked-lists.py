# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic={}
        while headA:
            dic[headA]=1
            headA=headA.next
        
        while headB:
            if dic.get(headB, 0):
                return headB
            headB=headB.next
        
        return None