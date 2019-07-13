# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.maxvalue = [[]]

	def getMaxValue(self, values,rows,cols):
		# write code here
		if rows <= 0 or cols <= 0:
			return 
		j =0
		while j <= cols-1:
			i = 0
			while i <= rows-1:
				if i-1 >= 0:
					down = self.maxvalue[j][i-1]
				else:
					down = 0
				if j-1 >= 0:
					right = self.maxvalue[j-1][i]
				else:
					right = 0
				self.maxvalue[j].append(max(down,right)+values[cols-1-j][rows-1-i])
				i += 1
			self.maxvalue.append([])
			j += 1
		return self.maxvalue[-2][-1]

# s = [[1,12,5,7],[10,2,7,7],[3,9,4,16],[8,6,11,5]]
s = [[7]]
t = Solution()
a = t.getMaxValue(s,1,1)
print(a)
