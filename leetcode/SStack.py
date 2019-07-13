class StackUnderFlow(ValueError):
	"""docstring for StackUnderFlow"""
	pass

class SStack(object):
	"""docstring for SStack"""
	def __init__(self):
		self._elems = []

	def is_empty(self):
		return self._elems == []
		
	def top(self):
		if self._elems == []:
			raise StackUnderFlow('in SStack.top()')
		return self._elems[-1]

	def push(self,x):
		return self._elems.append(x)

	def pop(self) -> object:
		if self._elems == []:
			raise StackUnderFlow('in SStack.pop()')
		return self._elems.pop()

st1 = SStack()
st1.push(3)
st1.push(5)
while not st1.is_empty():
	print(st1.pop())

