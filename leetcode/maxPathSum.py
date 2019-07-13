# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        def helper(node):
            if not node:
                return [None, 0]
            lp, rp = helper(node.left), helper(node.right)
            np = node.val + max(lp[1], rp[1])
            return [max(node.val + lp[1] + rp[1], lp[0], rp[0]), np if np > 0 else 0]
        return helper(root)[0]