# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		res = ListNode(0)
		p = res
		while l1 is not None and l2 is not None:
			p.next = ListNode(0)
			p.next.val += l1.val+l2.val
			p = p.next
			l1 = l1.next
			l2 = l2.next
		if l1 is None and l2 is None:
			pass
		elif l1 is None:
			p.next = l2
		else:
			p.next = l1
		q = res
		while q is not None:
			if q.val >= 10:
				if q.next is None:
					q.next = ListNode(0)
				q.next.val += q.val//10
				q.val = q.val%10
			q = q.next
		return res.next