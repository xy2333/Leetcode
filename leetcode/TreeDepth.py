# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
	def TreeDepth(self, pRoot):
		# write code here
		if pRoot is None: 
			return 0
		left = self.TreeDepth(pRoot.left)
		right = self.TreeDepth(pRoot.right)
		return max(left,right)+1