# def question1(num):
# 	res = ''
# 	while num > 0:
# 		if num%2 == 1:
# 			res += '1'
# 			num = num//2
# 		else:
# 			res += '2'
# 			num = num//2-1
# 	return res[::-1]

# print(question1(10))


# def question2(num):
# 	nstr = str(num)
# 	re_nstr = nstr[::-1]
# 	re_num = int(re_nstr)
# 	return re_num+num
# print(question2(0))




# def question5(lst,N):
# 	length = N
# 	for i in range(N):
# 		if lst[i]%4 == 0:
# 			lst[i] = 2
# 		elif lst[i]%2 == 0:
# 			lst[i] = 1
# 		else:
# 			lst[i] = 0
# 	num_0 = lst.count(0)
# 	num_2 = lst.count(2)
# 	if num_2 >= num_0:
# 		return 'Yes'
# 	else:
# 		return 'No'

# # a = question5([1,2,3,4],4)
# # print(a)

# m = input()
# while 1:
#     try:
#         N = int(input().strip())
#         lst =[int(i) for i in input().strip().split()]
#     except:
#         break
#     a = question5(lst,N)
#     print(a)


# def question7(lst,N):
# 	dp = [[0 for i in range(N+1)] for j in range(N+1)]
# 	dp[0][0] = dp[1][0] = dp[0][1] = 0
# 	for i in range(1,N):
# 		dp[i+1][0] = dp[0][i+1] = dp[i][0] + abs(lst[i]-lst[i-1])

# 	for i in range(1,N+1):
# 		for j in range(1,N+1):
# 			if i == j:
# 				pass
# 			elif i-1 == j:
# 				mindiff = min([dp[j][k]+abs(lst[i-1]-lst[k-1]) for k in range(1,j)]+[dp[j][0]])

# 				dp[j][i] = mindiff

# 			elif i+1 == j:
# 				mindiff = min([dp[k][i]+abs(lst[j-1]-lst[k-1]) for k in range(1,i)]+[dp[0][i]])

# 				dp[j][i] = mindiff

# 			else:
# 				if i > j:
# 					dp[j][i] = dp[j][i-1]+abs(lst[i-1]-lst[i-2])

# 				else:
# 					dp[j][i] = dp[j-1][i]+abs(lst[j-1]-lst[j-2])

# 	return min(dp[-1][:-1]+[dp[i][-1] for i in range(N)])


# # lst =[int(i) for i in '24 13 2 4 54 23 12 53 12 23 42 13 53 12 24 12 11 24 42 52 12 32 42'.strip().split()]
# lst = [1,5,6,2,1]
# a = question7(lst,5)
# print(a)

# def LCS(s1,s2):
# 	if s1 == '' or s2 == '':
# 		return 0
# 	l1 = len(s1)
# 	l2 = len(s2)
# 	dp = [[0]*(l1+1) for i in range(l2+1)]
# 	for i in range(1,l1+1):
# 		for j in range(1,l2+1):
# 			if s1[i-1] == s2[j-1]:
# 				dp[j][i] = dp[j-1][i-1]+1
# 			else:
# 				dp[j][i] = max(dp[j-1][i],dp[j][i-1])
# 	return dp[-1][-1]

# s1 = 'baedw'
# s2 = 'bcdae'
# a = LCS(s1, s2)
# print(a)


# def question6(s):
# 	if s == '':
# 		return 0
# 	res = set()
# 	res.add(s)
# 	for i in range(len(s)):
# 		lst = list(s)
# 		temp = lst.pop(i)
# 		for j in range(len(s)):
# 			lst.insert(j,temp)
# 			if is_right(lst):
# 				res.add(''.join(lst))
# 			lst.pop(j)
# 	return len(res)-1

# def is_right(s):
# 	num = 0
# 	for i in s:
# 		if i == '(':
# 			num += 1
# 		else:
# 			num -=1
# 			if num < 0:
# 				return False
# 	if num == 0:
# 		return True
# 	else:
# 		return False



# s = '(())'
# a = question6(s)
# print(a)

# def question8(N,x,y):
# 	if N <= 3:
# 		return N
# 	maxnum = 3
# 	for i in range(N):
# 		for j in range(i+1,N):
# 			for k in range(j+1,N):
# 				num = 3
# 				for m in range(k+1,N):
# 					if (y[m]-y[i])*(x[j]-x[i]) == (y[j]-y[i])*(x[m]-x[i]) or (y[k]-y[m])*(y[j]-y[i]) == -(x[k]-x[m])*(x[j]-x[i]):
# 						num += 1
# 				if num > maxnum:
# 					maxnum = num
# 	return maxnum



# N = 6
# x = [0,-1,1,1,-1,2]
# y = [0,-1,-1,1,1,2]
# a = question8(N,x,y)
# print(a)


def question4(n,L,city):
	Tree = {}
	Tree[0] = 0
	for i in range(n-1):
		Tree[i+1] = Tree[city[i]]+1
	deep = 0
	for d in Tree:
		if Tree[d] > deep:
			deep = Tree[d]
	if L <= deep:
		return L+1
	else:
		return min(n,1+deep+(L-deep)//2)

city = [0,1,2,3]
a = question4(5,2,city)
print(a)


while 1:
	try:
		[n,L] = [int(i) for i in input().strip().split()]
		city = [int(i) for i in input().strip().split()]
	except:
		break
	print(question4(n,L,city))
