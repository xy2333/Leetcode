# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    # 返回对应节点TreeNode
	def __init__(self):
		self.num = 0
		self.TreeNode = None

	def KthNode(self, pRoot, k):
		# write code here
		self.num = k
		self.midorder(pRoot)
		return self.TreeNode


	def midorder(self,pRoot):
		if pRoot is None or self.TreeNode is not None:
			return
		self.midorder(pRoot.left)
		self.num -= 1
		if self.num == 0:
			self.TreeNode = pRoot
		self.midorder(pRoot.right)

s = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
t = Solution()
a = t.KthNode(s,3)
print(a)
