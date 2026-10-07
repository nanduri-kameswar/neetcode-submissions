# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []
        count = 0
        # Inorder Traversal (LEFT -> NODE -> RIGHT)
        while current or stack:
            # move left
            while current:
                stack.append(current)
                current = current.left
            
            # process current node
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            # move right
            current = current.right
        
        return -1