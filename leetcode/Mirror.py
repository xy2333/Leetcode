# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        self.preorder(root,self.mirrornode)
    
    def preorder(self,t,mirrornode):
    	if t is None:
    		return 
    	mirrornode(t)
    	self.preorder(t.left,mirrornode)
    	self.preorder(t.right,mirrornode)

    def mirrornode(self,t):
    	t.left,t.right = t.right,t.left

