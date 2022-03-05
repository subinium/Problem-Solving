# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(node):
            if not node:
                return 0
            return node.val + getNum(node.next)*10

        val = getNum(l1)+getNum(l2)
        if val == 0:
            ret = [ListNode(0)]
        else:
            ret = []
        while val:
            ret.append(ListNode(val % 10))
            val //= 10

        for i in range(0, len(ret)-1):
            ret[i].next = ret[i+1]

        return ret[0]
