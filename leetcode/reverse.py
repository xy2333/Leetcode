class Solution:
	# def reverse(self, x):
	# 	"""
	# 	:type x: int
	# 	:rtype: int
	# 	"""
	# 	intmax = 2**31-1
	# 	intmin = -2**31
	# 	rev = 0
	# 	if x == 0:
	# 		return 0
	# 	if x > 0:
	# 		while x != 0:
	# 			pop = x%10
	# 			x = x//10
	# 			if rev*10 > intmax or (rev*10 == intmax and pop > 7):
	# 				return 0
	# 			else:
	# 				temp = rev*10+pop
	# 				rev = temp
	# 		return rev

	# 	if x < 0:
	# 		x = -x
	# 		while x != 0:
	# 			pop = x%10
	# 			x = x//10
	# 			if rev*10 > intmax or (rev*10 == intmax and pop > 8):
	# 				return 0
	# 			else:
	# 				temp = rev*10+pop
	# 				rev = temp
	# 		return -rev
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		intmax = 2**31-1
		intmin = -2**31
		if x>intmax or x<intmin:
			return 0
		if x >= 0:
			strs = str(x)
			restrs = strs[::-1]
			rex = int(restrs)
		else:
			x = abs(x)
			strs = str(x)
			restrs = strs[::-1]
			rex = -int(restrs)
		if rex>intmax or rex<intmin:
			return 0
		return rex

s = 1534236469
t = Solution()
a=t.reverse(s)
print(a)


