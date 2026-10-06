# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge Cases
        if not subRoot: return True
        if not root: return False

        # Base Case
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursive Case
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        # Base Case
        if not a and not b:
            return True
        # Recursive Case
        if a and b and (a.val == b.val):
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        # No match case
        return False