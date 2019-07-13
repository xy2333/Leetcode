class Solution:
	# def myAtoi(self, strs):
	# 	"""
	# 	:type str: str
	# 	:rtype: int
	# 	"""
	# 	flag = 0
	# 	intmin = -2**31
	# 	intmax = 2**31-1
	# 	strs = strs.strip(' ')
	# 	if len(strs) == 0 or not any(char.isdigit() for char in strs):
	# 		return 0
	# 	if strs[0] != '-' and not strs[0].isdigit() and strs[0] != '+':
	# 		return 0
	# 	for s in strs:
	# 		if s.isdigit():
	# 			start = strs.index(s)
	# 			for s in strs[start:]:
	# 				if not s.isdigit():
	# 					end = strs.index(s)
	# 					intnum = int(strs[start:end])
	# 					flag = 1
	# 					break
	# 			if flag == 0:
	# 				intnum = int(strs[start:])
	# 			break
	# 		elif s == '-':
	# 			if strs[strs.index(s)+1].isdigit():
	# 				start = strs.index(s)
	# 				for s in strs[start+1:]:
	# 					if not s.isdigit():
	# 						end = strs.index(s,start+1)
	# 						intnum = int(strs[start:end])
	# 						flag = 1
	# 						break
	# 				if flag == 0:
	# 					intnum = int(strs[start:])
	# 				break
	# 			else:
	# 				return 0
	# 		elif s == '+':
	# 			if not strs[strs.index(s)+1].isdigit():
	# 				return 0

	# 	if intnum < intmin:
	# 		return intmin
	# 	elif intnum > intmax:
	# 		return intmax
	# 	else:
	# 		return intnum
	def myAtoi(self, strs):
		"""
		:type str: str
		:rtype: int
		"""
		import re
		intmin = -2**31
		intmax = 2**31-1
		m = re.match(r'^(\s*)([-+]{0,1})(\d+)',strs)
		if m == None:
			return 0
		else:
			intnum = int(m.group(2)+m.group(3))
		if intnum < intmin:
			return intmin
		elif intnum > intmax:
			return intmax
		else:
			return intnum







ip = '+-1'
t = Solution()
a=t.myAtoi(ip)
print(a)