# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums = set(nums)
        cur = head
        while cur:
            if cur.val in nums:
                if cur == head:
                    cur = cur.next
                    head = cur
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
