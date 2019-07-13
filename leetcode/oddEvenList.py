# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if head is None or head.next is None or head.next.next is None:
			return head
		startodd = p = head
		starteven = q = head.next
		while p is not None and p.next is not None:
			p.next = p.next.next
			prep = p
			p = p.next
			if q is not None and q.next is not None:
				q.next = q.next.next
				q = q.next
		if q is not None:
			q.next = None
		if p is not None:
			p.next = starteven
		else:
			prep.next = starteven
		return startodd		