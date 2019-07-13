 def bubble_sort(lst):
	for i in range(len(lst)-1):
		flag = 0
		for j in range(len(lst)-i-1):
			if lst[j] > lst[j+1]:
				lst[j],lst[j+1] = lst[j+1],lst[j]
				flag = 1
		if flag == 0:
			break

def select_sort(lst):
	for i in range(len(lst)-1):
		minindex = i
		for j in range(i+1,len(lst)):
			if lst[minindex] > lst[j]:
				minindex = j
		if i != minindex:
			lst[minindex],lst[i] = lst[i],lst[minindex]

def insert_sort(lst):
	if len(lst) <= 1:
		return
	for i in range(1,len(lst)):
		preindex = i-1
		cur = lst[i]
		while preindex >= 0 and lst[preindex] > cur:
			lst[preindex+1] = lst[preindex]
			preindex -= 1
		lst[preindex+1] = cur

def quick_sort(lst):
	def qsort_rec(lst,begin,end):
		if begin+1 >= end:
			return
		r = lst[begin]
		i = begin
		for j in range(i,end):
			if lst[j] < r:
				i += 1
				lst[i],lst[j] = lst[j],lst[i]
		lst[i],lst[begin] = lst[begin],lst[i]
		qsort_rec(lst,begin,i)
		qsort_rec(lst,i+1,end)

	qsort_rec(lst,0,len(lst))


def merge_sort(lst):
	def merge_pass(lfrom,lto,llen,slen):
		i = 0
		while i + 2*slen <= llen:
			merge(lfrom,lto,i,i+slen,i+2*slen)
			i = i + 2*slen
		if i+slen < llen:
			merge(lfrom,lto,i,i+slen,llen)
		else:
			lto[i:] = lfrom[i:]

	def merge(lfrom,lto,low,mid,high):
		i = low
		j = mid
		k = low
		while i < mid and j < high :
			if lfrom[i] <= lfrom[j] :
				lto[k] = lfrom[i]
				i += 1
			else:
				lto[k] = lfrom[j]
				j += 1
			k += 1
		while i < mid:
			lto[k] = lfrom[i]
			i += 1
			k += 1
		while j < high:
			lto[k] = lfrom[j]
			j += 1
			k += 1
	
	slen = 1
	llen = len(lst)
	templst = [None]*llen
	while slen < llen:
		merge_pass(lst,templst,llen,slen)
		slen *= 2
		merge_pass(templst,lst,llen,slen)
		slen *= 2

def heap_sort(lst):
	def max_heaptify(lst,i,heapsize):
		left = 2*i+1
		right = 2*i+2
		largest = i
		if left < heapsize and lst[left] > lst[i]:
			largest = left
		if right < heapsize and lst[right] > lst[largest]:
			largest = right
		if largest == i:
			return
		else:
			lst[largest],lst[i] = lst[i],lst[largest]
			max_heaptify(lst,largest,heapsize)

	def build_max_heap(lst):
		length = len(lst)
		for i in range((length-2)//2,-1,-1):
			max_heaptify(lst,i,length)

	if len(lst) == 0:
		return []
	build_max_heap(lst)
	length = len(lst)
	heapsize = length
	for i in range(length-1,0,-1):
		lst[0],lst[i] = lst[i],lst[0]
		heapsize -= 1
		max_heaptify(lst,0,heapsize)
	return lst




a = [1,3,5,2,4,6,9,10,11]
bubble_sort(a)
print(a)
print('*******************************')
b = list(range(10))
bubble_sort(b)
print(b)
print('*******************************')
a = [1,3,5,2,4,6,9,10,11]
select_sort(a)
print(a)
print('*******************************')
a = [1,3,5,2,4,6,9,10,11]
insert_sort(a)
print(a)
print('*******************************')
a = [1,3,5,2,4,6,9,10,11]
quick_sort(a)
print(a)
print('*******************************')
a = [1,3,5,2,4,6,9,10,11]
merge_sort(a)
print(a)
print('*******************************')
a = [1,3,5,2,4,6,9,10,11]
heap_sort(a)
print(a)