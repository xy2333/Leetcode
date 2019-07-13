# def question1(n):
# 	dp = [0]*(n+1)
# 	dp[0] = dp[1] = 1
# 	if n <= 1:
# 		return 1
# 	for i in range(2,n+1):
# 		dp[i] = sum(dp)
# 	return dp[n]
# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question1(n))

# def question2(n):
# 	dp = [0]*(n+1)
# 	dp[0] = 1
# 	money = [1,5,10,20,50,100]
# 	for i in range(6):
# 		for j in range(1,n+1):
# 			if j-money[i] >= 0:
# 				dp[j] = dp[j] + dp[j-money[i]]
# 			else:
# 				dp[j] = dp[j]
# 	return dp[n]


# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question2(n))

# def question3(n,lst):
# 	maxarea = 0
# 	for i in range(n):
# 		end = i
# 		while end+1 < n and lst[end+1] >= lst[i]:
# 			end += 1
# 		start = i
# 		while start-1 >= 0 and lst[start-1] >= lst[i]:
# 			start -= 1
# 		wide = end-start+1
# 		area = wide*lst[i]
# 		maxarea = max(maxarea,area)
# 	return maxarea
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = [int(i) for i in input().strip().split()]
# 	except:
# 		break
# 	print(question3(n,lst))

def question4(s1,s2):
	ls1 = len(s1)
	ls2 = len(s2)
	if ls1 == 0 or ls2 == 0:
		return 0
	if ls1 <= ls2 :
		short = s1
		lshort = ls1
		longth = s2
		llongth = ls2
	else:
		short = s2
		lshort = ls2
		longth = s1
		llongth = ls1
	maxsame = 0
	for i in range(llongth):
		if i < lshort:
			same = findmax(short[-(i+1):],longth[:i+1])
		else:
			same = findmax(short,llongth[i-lshort+1:i+1])
		maxsame = max(same,maxsame)
	for i in range(lshort):
		same = findmax(short[:lshort-i],longth[-(lshort-i):])
		maxsame = max(same,maxsame)
	return maxsame


def findmax(s1,s2):
	maxl = 0
	l = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			l += 1
		else:
			maxl = max(maxl,l)
			l = 0
	maxl = max(maxl,l)
	return maxl

# print(findmax('1234','2344'))
print(question4('abcde','abgdeabcde'))