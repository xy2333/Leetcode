# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x, next_=None, random=None):
        self.label = x
        self.next = next_
        self.random = random


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ComplexListNode(pHead)

    def CloneNodes(self, pHead):
        while pHead is not None:
            a = pHead
            pHead = pHead.next
            a.next = RandomListNode(a.label)
            a = a.next
            a.next = pHead

    def ConnectSiblingNodes(self, pHead):
    	while pHead is not None:
    		if pHead.random is not None:
	    		pHead.next.random = pHead.random.next
    		pHead = pHead.next.next

    def ComplexListNode(self,pHead):
    	if pHead is None:
    		new = None
    		return new
    	old = pHead
    	new = pHead.next
    	i = old
    	j = new
    	while pHead.next.next is not None:
    		i.next = pHead.next.next
    		j.next = i.next.next
    		i = i.next
    		j = j.next
    		pHead = i
    	i.next = None
    	j.next = None
    	pHead = old
    	return new

    def printall(self, pHead):
        while pHead is not None:
        	if pHead.random is not None:
	            print(pHead.label, pHead.random.label)
	        else:
	        	print(pHead.label, None)
	       	pHead = pHead.next


A = RandomListNode(1)
B = RandomListNode(2)
C = RandomListNode(3)
D = RandomListNode(4)
E = RandomListNode(5)
A.next = B
B.next = C
C.next = D
D.next = E
A.random = C
B.random = E
D.random = B
t = Solution()
# t.printall(A)
# print('***************************')
# t.CloneNodes(A)
# t.printall(A)
# print('***************************')
# t.ConnectSiblingNodes(A)
# t.printall(A)
# print('***************************')
# a = t.ComplexListNode(A)
# t.printall(a)
t.printall(A)
print('***************************')
a = t.Clone(A)
t.printall(a)
