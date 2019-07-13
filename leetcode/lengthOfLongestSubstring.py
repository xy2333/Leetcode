class Solution:
	# def lengthOfLongestSubstring(self, s):
	# 	global diffnum
	# 	lennum = len(s)
	# 	ans = []
	# 	if lennum == 0:
	# 		return 0
	# 	elif lennum == 1:
	# 		return 1
	# 	else:
	# 		for i in range(lennum-1):
	# 			diffnum = 0
	# 			for j in range(i,lennum):
	# 				if s[j] not in s[i:j]:
	# 					diffnum = diffnum+1
	# 				else:
	# 					break
	# 			ans[i] = diffnum
	# 		return max(ans)

	# def lengthOfLongestSubstring(self, s):
	# 	if s == '':
	# 		return 0
	# 	longest_len = 1
	# 	curr = []
	# 	for x in s:
	# 		if x in curr:
	# 			index = curr.index(x)
	# 			curr = curr[index+1:]
	# 		curr.append(x)
	# 		if longest_len < len(curr):
	# 			longest_len = len(curr)
	# 	return longest_len
	def lengthOfLongestSubstring(self, s):
		lens = len(s)
		if len(s) == 0:
			return 0
		elif len(s) == 1:
			return 1
		else:
			i = 0
			j = 1
			maxlength = 1
			while 1:
				if s[j] not in s[i:j]:
					j += 1
				else:
					i+=1
				if j-i > maxlength:
					maxlength = j-i
				if j >= lens:
					return maxlength


s = 'aa'
t = Solution()
a=t.lengthOfLongestSubstring(s)
print(a)