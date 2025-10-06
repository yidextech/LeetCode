# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        i = 0
        j = k-1
        while i<len(res) and j < len(res):
            res[i:j+1] = res[i:j+1][::-1]
            i = j+1
            j = i+k-1
        
        new_head = ListNode(-1)
        cur = new_head
        for r in res:
            cur.next = ListNode(r)
            cur = cur.next
        return new_head.next

