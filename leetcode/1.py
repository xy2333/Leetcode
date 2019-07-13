# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x,next_ = None):
        self.val = x
        self.next = next_

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0:
        	return None
        if head is None:
        	return None
        i = 1
        j = 1
        ihead = head


        jhead = head
        while j < k and jhead is not None:
        	jhead = jhead.next
        	j += 1
        if j != k:
        	return None
        while jhead.next is not None:
        	jhead = jhead.next
        	j += 1
        	ihead = ihead.next
        	i += 1
        return ihead.val

dsf 
dsf 
dsf l
jsdlf 


