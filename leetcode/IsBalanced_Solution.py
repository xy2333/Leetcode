# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
	def __init__(self):
		self.flag = 0

	def IsBalanced_Solution(self, pRoot):
		# write code here
		temp = self.TreeDepth(pRoot)
		if self.flag == 1:
			return False
		else:
			return True

	def TreeDepth(self, pRoot):
		# write code here
		if self.flag == 1:
			return -1
		if pRoot is None: 
			return 0
		left = self.TreeDepth(pRoot.left)
		right = self.TreeDepth(pRoot.right)
		if abs(left-right) > 1:
			self.flag = 1
		return max(left,right)+1		

s = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
b = TreeNode(1,TreeNode(2,TreeNode(3)))
t = Solution()
a = t.IsBalanced_Solution(b)
print(a)
