# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def solve(nodeL, nodeR):
            if nodeL == None and nodeR == None:
                return True
            if nodeL == None or nodeR == None:
                return False

            if nodeL.val != nodeR.val:
                return False
            outside = solve(nodeL.left, nodeR.right)
            inside = solve(nodeL.right, nodeR.left)

            return outside and inside
        return solve(root.left, root.right)
        