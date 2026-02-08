# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def solve(node):
            ans = True
            
            if node == None:
                return 0
            leftH = solve(node.left)
            rightH = solve(node.right)

            if leftH == -1 or rightH == -1 or abs(leftH - rightH) > 1:
                return -1
            return max(leftH, rightH)+1
        return solve(root)!=-1
        