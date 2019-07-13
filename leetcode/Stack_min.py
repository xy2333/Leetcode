# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, node):
		# write code here
		self.stack.append(node)
		if not self.min_stack or self.min_stack[-1] >= node:
			self.min_stack.append(node)
		else:
			self.min_stack.append(self.min_stack[-1])
	def pop(self):
		# write code here
		if len(self.stack) == 0:
			return
		self.min_stack.pop()
		return self.stack.pop()
	def top(self):
		# write code here
		pass
	def min(self):
		# write code here
		if len(self.min_stack) == 0:
			return None
		return self.min_stack[-1]


t = Solution()
t.push(3)
t.push(2)
t.pop()
a = t.min()
print(a)




