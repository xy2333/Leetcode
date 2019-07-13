# -*- coding:utf-8 -*-
class ListNode:
	"""docstring for ListNode"""
	def __init__(self, data,next_ = None):
		self.data = data
		self.next = next_

class Solution:
	def LastRemaining_Solution(self, n, m):
		# write code here
		if m <= 0 or n <= 0:
			return -1
		if n <= 1:
			return 0 
		temp = pHead = ListNode(0)
		for i in range(1,n):
			pHead.next = ListNode(i)
			pHead = pHead.next
		pHead.next = temp
		pre_pHead = pHead
		pHead = pHead.next
		while pre_pHead != pHead:
			for j in range(m-1):
				pre_pHead = pre_pHead.next
				pHead = pHead.next
			pHead = pHead.next
			pre_pHead.next = pHead
		return pHead.data


t = Solution()
a = t.LastRemaining_Solution(5,3)
print(a)