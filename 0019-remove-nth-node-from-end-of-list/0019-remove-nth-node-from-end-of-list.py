# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find total length
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        n = count-n #index to remove 
        if n == 0:
            return head.next
        i = 0
        cur = head
        while cur:
            if i == (n-1):
                cur.next = cur.next.next
                return head
            cur = cur.next
            i += 1
            
