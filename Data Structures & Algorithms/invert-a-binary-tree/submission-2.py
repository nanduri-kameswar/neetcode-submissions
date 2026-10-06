# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base condition
        if not root:
            return None

        # Do it recursively for both branches
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Actual work
        root.left, root.right = right, left

        return root