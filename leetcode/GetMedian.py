# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.max_heap = []
		self.min_heap = []

	# def Insert(self,num):
	# 	for i in num:
	# 		self.insert(i)

	def Insert(self, num):
		# write code here
		if len(self.max_heap) == len(self.min_heap):
			self.insert_max_heap(num)
			return
		if len(self.max_heap) > len(self.min_heap):
			self.insert_min_heap(num)
			return

	def GetMedian(self):
		# write code here
		if len(self.max_heap) == len(self.min_heap):
			if len(self.max_heap) == 0:
				return None
			else:
				return (self.max_heap[0]+self.min_heap[0])/2.0
		else:
			return self.max_heap[0]

	def insert_max_heap(self,num):
		self.min_heap.append(num)
		self.min_heaptify_BottomToTop(len(self.min_heap)-1)
		a = self.delete_min_heap()
		self.max_heap.append(a)
		self.max_heaptify_BottomToTop(len(self.max_heap)-1)

	def insert_min_heap(self,num):
		self.max_heap.append(num)
		self.max_heaptify_BottomToTop(len(self.max_heap)-1)
		a = self.delete_max_heap()
		self.min_heap.append(a)
		self.min_heaptify_BottomToTop(len(self.min_heap)-1)

	def delete_min_heap(self):
		if len(self.min_heap) == 1:
			maxnum = self.min_heap.pop()
			return maxnum
		self.min_heap[0],self.min_heap[-1] = self.min_heap[-1],self.min_heap[0]
		maxnum = self.min_heap.pop()
		self.min_heaptify_TopToBotton(0)
		return maxnum

	def delete_max_heap(self):
		if len(self.max_heap) == 1:
			minnum = self.max_heap.pop()
			return minnum
		self.max_heap[0],self.max_heap[-1] = self.max_heap[-1],self.max_heap[0]
		minnum = self.max_heap.pop()
		self.max_heaptify_TopToBotton(0)
		return minnum

	def min_heaptify_BottomToTop(self,i):
		if i == 0:
			return
		index = i
		p = (index-1)//2
		minindex = p
		if p >= 0 and self.min_heap[p] > self.min_heap[index]:
			minindex = index
		if minindex == p:
			return
		else:
			self.min_heap[p],self.min_heap[index] = self.min_heap[index],self.min_heap[p]
			self.min_heaptify_BottomToTop(p)

	def max_heaptify_BottomToTop(self,i):
		if i == 0:
			return
		index = i
		p = (index-1)//2
		maxindex = p
		if p >= 0 and self.max_heap[p] < self.max_heap[index]:
			maxindex = index
		if maxindex == p:
			return
		else:
			self.max_heap[p],self.max_heap[index] = self.max_heap[index],self.max_heap[p]
			self.max_heaptify_BottomToTop(p)

	def min_heaptify_TopToBotton(self,i):
		length = len(self.min_heap)
		left = 2*i+1
		right = 2*i+2
		minindex = i
		if left < length and self.min_heap[left] < self.min_heap[minindex]:
			minindex = left
		if right < length and self.min_heap[right] < self.min_heap[minindex]:
			minindex = right
		if minindex == i:
			return
		else:
			self.min_heap[minindex],self.min_heap[i] = self.min_heap[i],self.min_heap[minindex]
			self.min_heaptify_TopToBotton(minindex)

	def max_heaptify_TopToBotton(self,i):
		length = len(self.max_heap)
		left = 2*i+1
		right = 2*i+2
		maxindex = i
		if left < length and self.max_heap[left] > self.max_heap[maxindex]:
			maxindex = left
		if right < length and self.max_heap[right] > self.max_heap[maxindex]:
			maxindex = right
		if maxindex == i:
			return
		else:
			self.max_heap[maxindex],self.max_heap[i] = self.max_heap[i],self.max_heap[maxindex]
			self.max_heaptify_TopToBotton(maxindex)

# s = [5,2,3,4,1,6,7,0,8]
t = Solution()
for i in [5,2]:
	t.Insert(i)
a = t.GetMedian()
print(a)




# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.data = []
	def Insert(self, num):
		# write code here
		self.data.append(num)
	def GetMedian(self):
		# write code here
		lst = self.data
		k = len(lst)//2
		if len(lst)%2 == 0:
			return (self.findk(lst,int(len(lst)/2))+self.findk(lst,int(len(lst)/2)-1))/2
		else:
			return self.findk(lst,len(lst)//2)
	
	def findk(self,lst,k):
		def rec(lst,begin,end,k):
			if end-begin < 2:
				return lst[begin]
			r = lst[begin]
			i = begin
			for j in range(begin+1,end):
				if lst[j] < r:
					i += 1
					lst[i],lst[j] = lst[j],lst[i]
			lst[i],lst[begin] = lst[begin],lst[i]
			if i == k:
				return lst[k]
			elif i > k:
				return rec(lst,begin,i,k)
			else:
				return rec(lst,i+1,end,k)

		return rec(lst,0,len(lst),k)

t = Solution()
for i in [1,5,6,8,10,11]:
	t.Insert(i)
a = t.GetMedian()
print(a)