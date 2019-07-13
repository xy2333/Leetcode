def LCS(s1,s2):
	if len(s1) == 0 or len(s2) == 0:
		return 0
	dp = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
	dirc = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
	for j in range(1,len(s2)+1):
		for i in range(1,len(s1)+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]+1
				dirc[i][j] = 2
			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
				if dp[i][j] == dp[i-1][j]:
					dirc[i][j] = 1
				else:
					dirc[i][j] = 3
	i = len(s1)
	j = len(s2)
	res = ''
	while i > 0 and j>0:
		if dirc[i][j] == 2:
			res = s1[i-1]+res
			i -= 1
			j -= 1
		elif dirc[i][j] == 1:
			i -= 1
		else:
			j -= 1

	return dp[-1][-1],res

s1 = 'ABCBDAB'
s2 = 'BDCABA'
print(LCS(s1, s2))
