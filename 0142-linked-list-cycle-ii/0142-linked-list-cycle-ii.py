# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cycle = set()
        cur = head

        while cur:
            if cur in cycle:
                return cur

            cycle.add(cur)
            cur = cur.next