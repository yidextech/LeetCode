# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def len_counter(head, n):
            cur = head
            while cur:
                n += 1
                cur = cur.next
            return n
        
        lenA = len_counter(headA, 0)
        lenB= len_counter(headB, 0)
        curA = headA
        curB = headB

        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        else:
            for i in range(lenB-lenA):
                curB = curB.next

        while curA and curB:
            if curA == curB:
                return curA
            curA, curB = curA.next, curB.next
        
        