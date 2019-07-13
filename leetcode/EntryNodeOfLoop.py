# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x,next_ = None):
        self.val = x
        self.next = next_
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        mnode = self.meetnode(pHead)
        if mnode is None:
        	return None
        num = self.numnode(mnode)
        iHead = pHead
        jHead = pHead
       	for j in range(num):
       		jHead = jHead.next
       	while iHead != jHead:
       		jHead = jHead.next
       		iHead = iHead.next
       	return iHead

    def numnode(self,mnode):
    	a = mnode
    	num = 1
    	mnode = mnode.next
    	while a != mnode:
    		mnode = mnode.next
    		num += 1
    	return num

    def meetnode(self,pHead):
    	if pHead is None:
    		return None
    	pfast = pHead
    	pslow = pHead
    	while pfast is not None and pfast.next is not None:
    		pfast = pfast.next
    		pfast = pfast.next
    		pslow = pslow.next
    		if pfast == pslow:
    			return pfast
    	return None

t = Solution()
s = ListNode(1,ListNode(2))
m = ListNode(3,ListNode(4,ListNode(5,s)))
s = ListNode(1, ListNode(2,m))
m = ListNode(3,ListNode(4,ListNode(5,s)))
a = t.EntryNodeOfLoop(s)
print(a)