class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		d = {}
		for i in nums:
			d[i] = d.get(i,0)+1
		lst = list(d.items())
		def rec(lst,begin,end):
			if end-begin < 2:
				return begin
			r = lst[begin]
			i = begin
			for j in range(i+1,end):
				if lst[j][1] > r[1]:
					i += 1
					lst[i],lst[j] = lst[j],lst[i]
			lst[i],lst[begin] = lst[begin],lst[i]
			if i == k-1:
				return i
			elif i < k-1:
				return rec(lst,i+1,end)
			else:
				return rec(lst,begin,i)
		index = rec(lst,0,len(lst))
		res = [x[0] for x in lst[:index+1]]
		return res