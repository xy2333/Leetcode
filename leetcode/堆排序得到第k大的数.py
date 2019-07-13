def maxheap(i,lstk,heapsize):
	left = 2*i+1
	right = 2*i+2
	largest = i
	if left+1 <= heapsize and lstk[left] > lstk[i]:
		largest = left
	if right+1 <= heapsize and lstk[right] > lstk[largest]:
		largest = right
	if largest == i:
		return 
	else:
		lstk[i],lstk[largest] = lstk[largest],lstk[i]
		maxheap(largest,lstk,heapsize)
def build(lstk):
	heapsize = len(lstk)
	for i in range((len(lstk)-2)//2,-1,-1):
		maxheap(i,lstk,heapsize)
def findk(lst,k):
	if len(lst) < k:
		return
	lstk = lst[:k]
	heapsize = k
	build(lstk)
	for i in range(k,len(lst)):
		if lst[i] < lstk[0]:
			lstk[0] = lst[i]
			maxheap(0,lstk,heapsize)
	return lstk[0]

lst = [1,3,5,2,4,6,1,1,1]
a = findk(lst,6)
print(a)