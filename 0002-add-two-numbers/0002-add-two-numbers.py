# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1,i2 = "",""
        cur1, cur2 = l1, l2
        while cur1:
            i1+=str(cur1.val)
            cur1 = cur1.next
        while cur2:
            i2+=str(cur2.val)
            cur2 = cur2.next
        i1,i2 = int(i1[::-1]), int(i2[::-1])
        res = str(i1+i2)
        ## formation of liked list
        head = ListNode()
        cur = head
        for i in range(len(res)-1, -1, -1):
            cur.next =ListNode(int(res[i]))
            cur = cur.next
        return head.next