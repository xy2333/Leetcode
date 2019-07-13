class SQueueUnderflow(ValueError):
	"""docstring for SQueueUnderflow"""
	pass

class SQueue():
	"""docstring for SQueue"""
	def __init__(self,init_len = 8):
		self._len = init_len
		self._elems = [0]*init_len
		self._head = 0
		self._num = 0

	def is_empty(self):
		return self._num == 0

	def peek(self):
		if self.is_empty():
			raise SQueueUnderflow('in self.peek()')
		return self._elems[self._head]

	def dequeue(self):
		if self.is_empty():
			raise SQueueUnderflow('in self.dequeue()')
		e = self._elems[self._head]
		self._head += 1
		self._num -= 1 
		return e

	def enqueue(self,x):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head + self._num) % self._len] = x
		self._num += 1

	def __extend(self):
		old_len = self._len
		self._len = self._len*2
		new_elems = [0]*self._len
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head+i)%old_len]
		self._elems = new_elems
		self._head = 0

		
s = SQueue()
s.enqueue(3)
s.enqueue(5)
while not s.is_empty():
	print(s.dequeue())
