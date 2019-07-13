# -*- coding:utf-8 -*-
class Solution:
	def GetLeastNumbers_Solution(self, tinput, k):
		# write code here
		if len(tinput) < k:
			return []
		if len(tinput) == k:
			return sorted(tinput)
		begin = 0
		end = len(tinput)
		index = self.Partition(tinput, begin, end)
		while index != k:
			if index < k:
				begin = index+1
			else:
				end = index
			index = self.Partition(tinput, begin, end)
		return sorted(tinput[:index])

	def Partition(self,lst,begin,end):
		if begin >= end:
			return
		p = lst[begin]
		i = begin
		j = begin+1
		while j < end:
			if lst[j] >= p:
				j += 1
			else:
				lst[i+1],lst[j] = lst[j],lst[i+1]
				i += 1
				j += 1
		lst[begin],lst[i] = lst[i],lst[begin]
		return i

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def rec(tinput,k,begin,end):
            if begin+1 >= end:
                return tinput[:begin+1]
            r = tinput[begin]
            i = begin
            for j in range(i+1,end):
                if tinput[j] < r:
                    i += 1
                    tinput[i],tinput[j] = tinput[j],tinput[i]
            tinput[i],tinput[begin] = tinput[begin],tinput[i]
            if i+1 == k:
                return tinput[:i+1]
            elif i+1 < k:
                return rec(tinput,k,i+1,end)
            else:
                return rec(tinput,k,begin,i)
        
        return rec(tinput,k,0,len(tinput))
                

s = [4,5,1,6,2,7,3,8]
t = Solution()
a = t.GetLeastNumbers_Solution(s,8)
print(a)
