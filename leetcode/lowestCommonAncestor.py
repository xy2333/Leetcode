# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		if root is None:
			return None
		if root is p or root is q:
			return root
		L = self.lowestCommonAncestor(root.left,p,q)
		R = self.lowestCommonAncestor(root.right,p,q)
		if L is None and R is None:
			return None
		if L is None:
			return R
		if R is None:
			return L
		return root
