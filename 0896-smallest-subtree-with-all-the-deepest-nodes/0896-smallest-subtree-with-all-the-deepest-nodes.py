# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node: return (None, 0)
            lNode, lDist = dfs(node.left)
            rNode, rDist = dfs(node.right)

            if lDist>rDist:
                return(lNode, lDist+1)
            elif rDist>lDist:
                return(rNode,rDist+1)
            else:
                return (node, lDist+1)

        result_node, total_dist = dfs(root)
        return result_node