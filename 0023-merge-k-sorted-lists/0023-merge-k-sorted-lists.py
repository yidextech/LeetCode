# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #Merged 
        merged = []
        for l in lists:
            while l:
                merged.append(l.val)
                l = l.next
        merged.sort()
        head = ListNode()
        cur = head
        for m in merged:
            cur.next = ListNode(m) 
            cur = cur.next
        return head.next

