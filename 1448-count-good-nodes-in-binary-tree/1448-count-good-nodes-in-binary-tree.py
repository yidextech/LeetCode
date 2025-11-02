# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        dq = deque()
        low = float('-inf')
        dq.append( (root, low) )
        count = 0
        while dq:
            for i in range(len(dq)):
                cur = dq.pop()
                #check and append the children
                #cur[0] --> child and cur[1] --> parent 
                if cur[1]==low or cur[0].val >= cur[1].val:
                    count += 1
                if cur[0].left:
                    dq.append( (cur[0].left, cur[0]) )
                if cur[0].right:
                    dq.append( (cur[0].right, cur[0]) )
        return count