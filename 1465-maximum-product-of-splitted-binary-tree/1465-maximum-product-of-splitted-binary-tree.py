# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        allSum = []
        def tree_sum(node):
            if not node:
                return 0
            left_sum = tree_sum(node.left)
            right_sum = tree_sum(node.right)
            current_s = node.val + left_sum + right_sum
            
            allSum.append(current_s)
            return current_s
        
        totalSum = tree_sum(root)
        best = 0
        for s in allSum:
            currentProduct = s*(totalSum - s)
            best = max(currentProduct, best)
        return best %(10**9+7)
        