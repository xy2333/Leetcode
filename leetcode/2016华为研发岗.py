# class ListNode():
# 	"""docstring for ListNode"""
# 	def __init__(self,val,next_=None):
# 		self.val = val
# 		self.next = next_

# def question(n):
# 	if n > 1000:
# 		n = 1000
# 	phead = ListNode(0)
# 	p = phead
# 	for i in range(1,n):
# 		p.next_ = ListNode(i)
# 		p = p.next_
# 	p.next_ = phead
# 	while phead.next_ != phead:
# 		phead = phead.next_
# 		phead.next_ = phead.next_.next_
# 		phead = phead.next_
# 	return phead.val

# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question(n))

def question2(s):
	import collections
	d = collections.OrderedDict()
	for i in s:
		d[i] = 0
	return ''.join(d)
while 1:
	try:
		s = input().strip()
	except:
		break
	print(question2(s))


