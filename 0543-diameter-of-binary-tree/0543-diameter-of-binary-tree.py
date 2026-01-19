# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
        def solve(node):
            if node == None:
                return 0

            leftH = solve(node.left)
            rightH = solve(node.right)

            self.max_diameter = max(self.max_diameter, leftH + rightH)
            return 1+ max(leftH, rightH)

        solve(root)
        return self.max_diameter
        