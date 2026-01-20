# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, root, minV, maxV):
        if root == None:
            return True
        if root.val <= minV or root.val>=maxV:
            return False
        
        checkLeft = self.check(root.left, minV, root.val)
        checkRight = self.check(root.right, root.val, maxV)
        return checkLeft and checkRight

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check(root, float('-inf'), float('inf'))