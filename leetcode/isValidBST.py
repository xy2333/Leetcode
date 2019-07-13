# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isValidBST(self, root):
		if self.rec(root):
			return True
		else:
			return False


	def rec(self,root):
		if root is None:
			return [None,None]
		left = self.rec(root.left)
		right = self.rec(root.right)
		if left is False or right is False:
			return False
		if left[1] is None or left[1] < root.val:
			pass
		else:
			return False
		if right[0] is None or right[0] > root.val:
			pass
		else:
			return False
		res = [None,None]
		if left[0] is None:
			res[0] = root.val
		else:
			res[0] = left[0]
		if right[1] is None:
			res[1] = root.val
		else:
			res[1] = right[1]
		return res