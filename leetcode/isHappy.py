class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		history = set([n])
		res = sum([int(i)**2 for i in str(n)])
		while res not in history and res != 1:
			history.add(res)
			res = sum([int(i)**2 for i in str(res)])
		if res == 1:
			return True
		else:
			return False



        
        

s = 4

t = Solution()
res = t.isHappy(s)
print(res)
