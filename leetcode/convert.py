# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
	def __init__(self):
		self.lastnode = None

	def Convert(self, pRootOfTree):
		# write code here
		if pRootOfTree is None:
			return None
		self.midorder(pRootOfTree)
		while self.lastnode.left is not None:
			self.lastnode = self.lastnode.left
		return self.lastnode
	def midorder(self,pRootOfTree):
		if pRootOfTree is None:
			return
		self.midorder(pRootOfTree.left)
		if self.lastnode is not None:
			pRootOfTree.left = self.lastnode
			self.lastnode.right = pRootOfTree 
			self.lastnode = pRootOfTree
		else:
			self.lastnode = pRootOfTree
		self.midorder(pRootOfTree.right)

	def printall(self,t):
		if t is None:
			print(None)
			return
		else:
			while t is not None:
				print(t.val)
				t = t.right

 #    def rec(self,pRootOfTree):
 #    	if pRootOfTree is None :
 #    		return
 #    	leftchild = pRootOfTree.left
 #    	rightchild = pRootOfTree.right
 #    	leftmax = self.findmax(leftchild)
 #    	rightmin = self.findmin(rightchild)


 #    def findmax(self,t):
 #    	if t is None:
 #    		return None
 #    	while t is not None:
 #    		maxnode = t
 #    		t = t.right
 #    	return maxnode

	# def findmin(self,t):
 #    	if t is None:
 #    		return None
 #    	while t is not None:
 #    		minnode = t
 #    		t = t.left
 #    	return minnode

s = TreeNode(10, TreeNode(6, TreeNode(4), TreeNode(8)), TreeNode(14, TreeNode(12), TreeNode(16)))
t = Solution()
a = t.Convert(s)
t.printall(a)

