# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        def buildTree(preorder, inorder):
            if not preorder:
                return 
            
            rootValue = preorder[0]
            indx = inorder.index(rootValue)
            root = TreeNode(rootValue)


            left_inorder = inorder[:indx]
            n = len(left_inorder)
            left_preorder = preorder[1:n+1]
            
            right_inorder = inorder[1+indx:]
            right_preorder = preorder[n+1:]

            root.left = buildTree(left_preorder, left_inorder)
            root.right = buildTree(right_preorder, right_inorder)

            return root
        return buildTree(preorder, inorder)
