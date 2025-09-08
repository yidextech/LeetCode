# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        head = cur
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                cur.next = ListNode(cur2.val)
                cur2 = cur2.next
            cur = cur.next
        rem = cur1 if cur1 else cur2
        while rem:
            cur.next = ListNode(rem.val)
            cur = cur.next
            rem = rem.next
        return head.next
