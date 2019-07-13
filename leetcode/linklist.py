class Lnode(object):
	"""docstring for Lnode"""
	def __init__(self,elem,next_=None):
		self.elem = elem
		self.next = next_

class LinkedlistUnderflow(ValueError):
	"""docstring for LinkedlistUnderflow"""
	pass

class LList():
	"""docstring for LList"""
	def __init__(self):
		self._head = None
	
	def is_empty(self):
		return self._head is None

	def prepend(self,elem):
		self._head = Lnode(elem,self._head)

	def pop(self) -> object:
		if self._head is None:
			raise LinkedlistUnderflow('in pop')
		e = self._head.elem
		self._head = self._head.next
		return e

	def printall(self):
		p = self._head
		while p is not None:
			print(p.elem)
			p = p.next

	def append(self,elem):
		if self._head is None:
			self._head = Lnode(elem)
			return
		p = self._head
		while p.next is not None:
			p = p.next
		p.next = Lnode(elem)

	def pop_last(self):
		if self._head is None:
			raise LinkedlistUnderflow('in pop_last')
		p = self._head
		if self._head.next is None:
			e = p.elem
			self._head = None
			return e
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		return e
		
	def find(self,pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				return p.elem
			p = p.next

	def elements(self):
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next

	def filter(self,pred):
		p = self._head
		while p is not None :
			if pred(p.elem):
				yield p.elem
			p = p.next

	def rev(self):
		p = None
		while self._head is not None:
# q是数据结构的名，q对应的是地址
# q.elem和q.next是数据的名，对应的是实际的数
			q = self._head
			self._head = q.next
			q.next = p
			p = q
		self._head = p

	def sort(self):
		p = self._head
		if p is None or p.next is None:
			return
		rem = p.next
		while rem is not None:
			p = self._head
			q = None
			while p is not None and p.elem < rem.elem:
				q = p
				p = p.next
			if q is None:
				self._head = rem
			else:
				q.next = rem
			q = q.next
			rem = rem.next
			if p.next == rem:
				q.next = p.next
			else:
				q.next = p

	def sort1(self):
		if self._head is None:
			return
		crt = self._head.next
		while crt is not None:
			x = crt.elem
			p = self._head
			while p is not crt and p.elem <= x:
				p = p.next
			while p is not crt:
				y = p.elem
				p.elem = x
				x = y
				p = p.next
			crt.elem = x
			crt = crt.next








p = LList()
# p.pop()
for i in range(10):
	p.prepend(i)
p.printall()

print(p.is_empty())

e = p.pop()
p.printall()
print(e)
print('***********************')
p.append(-1)
p.printall()
print('***********************')
e = p.pop_last()
p.printall()
print('***********************')
print(e)
print('***********************')
pred = lambda x:x == 4
a = p.find(pred)
print(a)
print('***********************')
for i in p.elements():
	print(i)
print('***********************')
pred = lambda x : x%2 == 0
for i in p.filter(pred):
	print(i)
print('***********************')
p.rev()
p.printall()
print('***********************')
q = LList()
for i in [1,3,5,2,4,6]:
	q.append(i)
q.printall()
print('***********************')
q.sort1()
q.printall()





# q = Lnode(13)
# head = Lnode(1)
# q.next = head.next
# head.next = q
# print(q)
# print(q.next)
# print(head.next)

# linklist1 =  Lnode(0)
# p = linklist1
# for i in range(1,10):
# 	p.next = Lnode(i)
# 	p = p.next
# p = linklist1

# while p.next != None:
# 	print(p.elem)
# 	p = p.next
# 	pass
		