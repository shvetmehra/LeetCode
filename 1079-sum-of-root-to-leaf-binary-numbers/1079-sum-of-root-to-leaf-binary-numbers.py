# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.total = 0
        def solve(node, binary):
            if node is None:
                return 
            current_path = binary +str(node.val)
            if not node.left and not node.right:
                self.total += int (binary+str(node.val), 2)
                return
            solve(node.left, current_path)
            solve(node.right, current_path)
        solve(root, "")
        return self.total