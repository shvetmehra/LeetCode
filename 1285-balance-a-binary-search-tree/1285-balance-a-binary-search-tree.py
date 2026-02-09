# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        self.extracted_Sorted_elements(root, ans)
        return self.bulid_balanced_tree(ans, 0, len(ans)-1)

    def extracted_Sorted_elements(self, root, ans):
        if root is None:
            return
        self.extracted_Sorted_elements(root.left, ans)
        ans.append(root.val)
        self.extracted_Sorted_elements(root.right, ans)

    def bulid_balanced_tree(self,ans, start, end):
        if start>end:
            return None
        mid = (start+end)//2
        root = TreeNode(ans[mid])

        root.left = self.bulid_balanced_tree(ans, start, mid-1)
        root.right = self.bulid_balanced_tree(ans, mid+1, end)

        return root
                


        