# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        def bfs(root):
            dq = deque()
            dq.append(root)
            while dq:
                node = dq.popleft()
                if node:
                    r1.append(node.val)
                if not node:
                    r1.append("root")
                    return
                if node.left:
                    dq.append(node.left)
                if not node.left:
                    r1.append("L")
                if node.right:
                    dq.append(node.right)
                if not node.right:
                    r1.append("R")
        bfs(p)
        r2 = r1[:]
        r1 = []
        bfs(q)
        if r1==r2:
            return True
        return False
            
            