# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = deque()
        dq.append(root)
        h = 1
        while dq:
            for i in range(len(dq)):
                cur = dq.popleft()
                if not(cur.left or cur.right):
                    return h
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            h += 1