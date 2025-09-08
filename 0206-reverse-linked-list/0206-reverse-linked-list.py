# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None
        curr = head

        while curr:
            curr_node = curr
            next_node = curr.next
            curr_node.next = newhead
            newhead = curr
            curr = next_node
        return newhead

