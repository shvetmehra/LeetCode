# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        self.helper(root, ans)
        return self.balanced(ans)
    
    def helper(self, root, ans):
        if root is None:
            return 
        self.helper(root.left, ans)
        ans.append(root.val)
        self.helper(root.right, ans)

    def balanced(self, ans):
        if not ans:
            return
        mid = len(ans)//2
        root = TreeNode(ans[mid])
        root.left = self.balanced(ans[:mid])
        root.right = self.balanced(ans[mid+1:])
        return root
