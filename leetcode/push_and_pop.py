# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
	# write code here
		self.stack1.append(node)

	def pop(self) -> object:
	# return xx
		if self.stack2 == []:
			self.stack2 = self.stack1[::-1]
			self.stack1 = []
			return self.stack2.pop()
		else:
			return self.stack2.pop()

t = Solution()
t.push(3)
t.push(5)
print(t.pop())
print(t.pop())

