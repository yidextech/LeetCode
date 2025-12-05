# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = set()
        cur = head
        prev = None
        while cur:
            next= cur.next
            if cur.val in check:
                prev.next = next
            else:
                check.add(cur.val)
                prev = cur
            cur  = next
        return head