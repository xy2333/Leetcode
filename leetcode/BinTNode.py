class BinTNode(object):
	"""docstring for BinTNode"""
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

def count_BinTNodes(t):
	if t is None:
		return 0
	else:
		return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)

def sum_BinTNode(t):
	if t is None:
		return 0
	else:
		return t.data + sum_BinTNode(t.right) + sum_BinTNode(t.left)

def preorder(t,proc):
	if t is None:
		return
	proc(t.data)
	preorder(t.left,proc)
	preorder(t.right,proc)

def preorder_nonrec(t,proc):
	s = []
	while t is not None or len(s) != 0:
		while t is not None:
			# t.data = proc(t.data)
			proc(t.data)
			s.append(t.right)
			t = t.left
		t = s.pop()


def midorder(t,proc):
	if t is None:
		return
	preorder(t.left,proc)
	proc(t.data)
	preorder(right,proc)

def lastorder(t,proc):
	if t is None:
		return
	preorder(t.left,proc)
	preorder(t.right,proc)
	proc(t.data)

def print_BinTNodes(t):
	if t is None:
		print('^', end = '')
		return
	print('(' + str(t.data), end = '')
	print_BinTNodes(t.left)
	print_BinTNodes(t.right)
	print(')',end = '')

def preorder_elements(t):
	s = []
	while t is not None or len(s) != 0:
		while t is not None:
			s.append(t.right)
			yield t.data
			t = t.left
		t = s.pop()

a = BinTNode(1, BinTNode(2), BinTNode(3))
num = count_BinTNodes(a)
print(num)
print('*************************************')
sums = sum_BinTNode(a)
print(sums)
# print('*************************************')
# proc = lambda x : x**2
# preorder(a,proc)
# print(sum_BinTNode(a))
print('*************************************')
print_BinTNodes(a)
print('')
print('*************************************')
proc = lambda x : x**2
preorder_nonrec(a,proc)
print_BinTNodes(a)
print('')
print('*************************************')
for i in preorder_elements(a):
	print(i)
