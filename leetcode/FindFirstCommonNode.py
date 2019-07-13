# -*- coding:utf-8 -*-
class ListNode:
	def __init__(self, x,next_=None):
		self.val = x	
		self.next = next_
class Solution:
	def FindFirstCommonNode(self, pHead1, pHead2):
		# write code here
		if pHead1 is None or pHead2 is None:
			return None
		l1 = []
		l2 = []
		while pHead1 is not None:
			l1.append(pHead1)
			pHead1 = pHead1.next
		while pHead2 is not None:
			l2.append(pHead2)
			pHead2 = pHead2.next
		same = None
		while l1 and l2:
			a = l1.pop()
			b = l2.pop()
			if a != b:
				return same
			else:
				same = a
		return same

b = ListNode(3,ListNode(4))
a = ListNode(1,ListNode(2,b))
c = ListNode(5,b)

t = Solution()
a = t.FindFirstCommonNode(a,c)
print(a)