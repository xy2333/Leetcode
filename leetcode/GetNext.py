# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self，x，left = None,right = None,next_ = None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next_

class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
        	return None
        if pNode.right is not None:
        	tmp = pNode.right
        	while tmp.left is not None:
        		tmp = tmp.left
        	return tmp
        elif pNode.next is None:
        	return None
        # have family;right is empty
        if pNode.next.left == pNode:
        	return pNode.next
        if pNode.next.right == pNode:
        	while pNode.next.right == pNode:
        		pNode = pNode.next
        		if pNode.next is None:
        			return None
        	return pNode.next	

a = TreeLinkNode(1,TreeLinkNode(2),TreeLinkNode())