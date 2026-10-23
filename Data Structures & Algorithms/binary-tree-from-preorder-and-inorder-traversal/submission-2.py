# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Recursive Calls"""
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # root_idx = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        # root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1: ])
        # return root

        # value -> index in inorder, so root lookup is O(1) instead of O(n)
        idx = {val: i for i, val in enumerate(inorder)}
        pre_i = 0  # next root to consume from preorder

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal pre_i
            if lo > hi:  # empty inorder window -> no subtree
                return None

            root = TreeNode(preorder[pre_i])
            pre_i += 1

            mid = idx[root.val]
            root.left = build(lo, mid - 1) # must be built BEFORE right
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)
