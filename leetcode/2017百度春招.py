# def question1(lst):
# 	slst = set(lst)
# 	slslst = list(slst)
# 	sortlst = sorted(slslst)
# 	if len(sortlst) < 3:
# 		return -1
# 	else:
# 		return sortlst[2]

# # print(question1([10,10,10,10,20,20,30,30,40,40]))
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = [int(i) for i in input().strip().split()]
# 	except:
# 		break

# 	print(question1(lst))
# def question2(n,lst):
# 	if n <= 2:
# 		return abs(lst[0]-lst[1])
# 	sumdict = 0
# 	for j in range(1,n):
# 		sumdict += abs(lst[j]-lst[j-1])
# 	mindist = abs(lst[0]-lst[2])-abs(lst[0]-lst[1])-abs(lst[1]-lst[2])
# 	for i in range(1,n-1):
# 		dist = abs(lst[i-1]-lst[i+1])-abs(lst[i-1]-lst[i])-abs(lst[i]-lst[i+1])
# 		mindist = min(dist,mindist)
# 	return sumdict+mindist

# # print(question2(4,[1,4,-1,3]))
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = [int(i) for i in input().strip().split()]
# 	except:
# 		break

# 	print(question2(n,lst))
# import itertools
# # import numpy as np
# def dot(a,b):
# 	res = 0
# 	for i in range(len(a)):
# 		res += a[i]*b[i]
# 	return res

# def question3(n,lst):
# 	if n < 3:
# 		return 0
# 	combinations = itertools.combinations(lst,3)
# 	maxarea = 0
# 	for i in combinations:
# 		if (i[0][0] == i[1][0] and i[0][0] == i[2][0]) or (i[0][0] != i[1][0] and i[0][0] != i[2][0] and i[1][0] != i[2][0]) and (i[0][1:] != i[1][1:] and i[0][1:] != i[2][1:] and i[1][1:] != i[2][1:]):
# 			a = i[0][1:]
# 			b = i[1][1:]
# 			c = i[2][1:]
# 			a2b = [j[1]-j[0] for j in zip(a,b)]
# 			a2c = [j[1]-j[0] for j in zip(a,c)]
# 			proj_ab = dot(a2b,a2c)/(dot(a2c,a2c)**0.5)
# 			h = (dot(a2b,a2b)-proj_ab**2)**0.5
# 			area = h*(dot(a2c,a2c)**0.5)/2

# 			maxarea = max(maxarea,area) 
# 	return maxarea		
# # lst = [['R',0,0,0],['R',0,4,0],['R',0,0,3],['G',92,14,7],['G',12,16,8]]
# # res = question3(5,lst)
# # print('%.5f' % res)
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = []
# 		for i in range(n):
# 			dian = input().strip().split()
# 			lst.append([dian[0]]+[int(j) for j in dian[1:]])
# 	except:
# 		break
# 	res = question3(n,lst)
# 	print('%.5f' % res)

# def question4(n,lst):
# 	slst = sorted(lst)
# 	i = j = count = 0
# 	while i < n and j < n:
# 		if slst[i] == lst[j]:
# 			count += 1
# 			i += 1
# 			j += 1
# 		else:
# 			j += 1
# 	return n-count
# # print(question4(4,[7,8,19,25]))
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = [int(i) for i in input().strip().split()]
# 	except:
# 		break
# 	print(question4(n,lst))

# def question5(n,k):
# 	import itertools
# 	lst = list(range(1,n+1))
# 	permutation = itertools.permutations(lst,n)
# 	res = 0
# 	for m in permutation:
# 		count = 0
# 		for i in range(n-1):
# 			if m[i] < m[i+1]:
# 				count += 1
# 			if count > k:
# 				break
# 		if count == k:
# 			res += 1
# 	return res


# # print(question5(5,2))
# while 1:
# 	try:
# 		[n,k] = [int(i) for i in input().strip().split()]
# 	except:
# 		break

# 	print(question5(n,k))

def question5(n,k):
	dp = [[0]*k for i in range(n+1)]
	for i in range(n+1):
		dp[i][0] = 1
	for i in range(2,n+1):
		for j in range(1,k+1):
			dp[i][j] = dp[i-1][j]*(j+1)+dp[i-1][j-1]*(i-j)
	return dp[n][k]%2017
while 1:
	try:
		[n,k] = [int(i) for i in input().strip().split()]
	except:
		break

	print(question5(n,k))
