# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
	def __init__(self):
		self.stack = []
		self.res = [[]]
	def Print(self, pRoot):
		# write code here
		if pRoot is not None:
			self.stack.append(pRoot)
		now = 1
		last = 0
		while len(self.stack) != 0:
			temp = self.stack.pop(0)
			now -= 1
			self.res[-1].append(temp.val)
			if temp.left is not None:
				self.stack.append(temp.left)
				last += 1
			if temp.right is not None:
				self.stack.append(temp.right)
				last += 1
			if now == 0:
				now = last
				last = 0
				self.res.append([])
		res = self.res[:-1]
		for i in range(len(res)):
			if i%2 == 1:
				res[i] = res[i][::-1]
		return res