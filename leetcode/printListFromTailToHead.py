# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self,x,next_=None):
    	self.val = x
    	self.next = next_
# class Lnode(object):
# 	"""docstring for Lnode"""
# 	def __init__(self, elem,next_ = None):
# 		self.elem = elem
# 		self.next = next_

# class LList():
# 	"""docstring for LList"""
# 	def __init__(self):
# 		self._head = None

# 	def prepend(self,elem):
# 		self._head = Lnode(elem,self._head)

# 	def revprintall():
# 		while self._head is None:
# 			return 
# 		p = self._head
# 		valuelist = []
# 		while p is not None:
# 			valuelist.append(p.elem)
# 			p = p.next
# 		print(valuelist[::-1])						

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        while listNode is None:
        	return []
        p = listNode
        valuelist = []
        while p is not None:
        	valuelist.append(p.val)
        	p = p.next
        return valuelist[::-1]
        
p = None
# for i in range(1,10):
# 	p = ListNode(i,p)

t = Solution()
a = t.printListFromTailToHead(p)
print(a)