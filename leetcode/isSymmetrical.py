# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        list1 = []
        list2 = []
        self.preorder(pRoot, list1)
        self.preorder2(pRoot,list2)
        return list1 == list2

    def preorder(self,t,list1):
    	if t is None:
    		list1.append(None)
    		return
    	list1.append(t.val)
    	self.preorder(t.left,list1)
    	self.preorder(t.right,list1)

    def preorder2(self,t,list2):
    	if t is None:
    		list2.append(None)
    		return
    	list2.append(t.val)
    	self.preorder2(t.right,list2)
    	self.preorder2(t.left,list2)


Tree = TreeNode(8, TreeNode(8,TreeNode(9),TreeNode(2,TreeNode(4),TreeNode(7))), TreeNode(7))
t = Solution()
a = t.isSymmetrical(Tree)
print(a)