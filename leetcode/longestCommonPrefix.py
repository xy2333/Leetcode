class Solution:
	# def longestCommonPrefix(self, strs):
	# 	"""
	# 	:type strs: List[str]
	# 	:rtype: str
	# 	"""
	# 	if not strs:
	# 		return ''
	# 	elif len(strs) == 1:
	# 		return strs[0]
	# 	samestr = ''
	# 	for i in range(len(strs[0])):
	# 		for j in range(1, len(strs)):
	# 			if len(strs[j]) > i:
	# 				if strs[0][i] == strs[j][i]:
	# 					if j == len(strs) - 1:
	# 						samestr += strs[0][i]
	# 				else:
	# 					return samestr
	# 			else:
	# 				return samestr
	# 	return samestr

	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0:
			return ''
		if min(list(map(lambda x:len(x),strs))) == 0:
			return ''
		length = 0
		for j in range(min(list(map(lambda x:len(x),strs)))):
			m = list(map(lambda i:strs[i][j],range(len(strs))))
			if m.count(m[0]) == len(m):
				length += 1
			else:
				return strs[0][:length]
		return strs[0][:length]





s = ["c"]
t = Solution()
a = t.longestCommonPrefix(s)
print(a)
