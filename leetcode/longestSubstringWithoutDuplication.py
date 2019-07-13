# -*- coding:utf-8 -*-
class Solution:
	def longestSubstringWithoutDuplication(self, strs):
		# write code here
		length = len(strs)
		if length == 0:
			return 0
		if length == 1:
			return 1
		i,j = 0,1
		maxlength = 1
		while j < length:
			if strs[j] not in strs[i:j]:
				j += 1
				maxlength = max(maxlength,j-i)
			else:
				while i < j and strs[j] in strs[i:j]:
					i += 1
				if  i == j:
					j += 1
		return maxlength					

s = 'bb'
t = Solution()
a = t.longestSubstringWithoutDuplication(s)
print(a)
