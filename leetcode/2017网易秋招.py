# def question(lst):
# 	if len(lst) == 1 or len(lst) == 0:
# 		return 0
# 	if lst[0] == lst[-1]:
# 		return question(lst[1:-1])
# 	elif lst[0] > lst[-1]:
# 		lst[-2] = lst[-2]+lst[-1]
# 		return 1+question(lst[:-1])
# 	else:
# 		lst[1] = lst[0]+lst[1]
# 		return 1+question(lst[1:])		
# # lst = [1,2,3,4]
# # print(question(lst))
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = [int(i) for i in input().strip().split()]
# 	except:
# 		break
# 	print(question(lst))


# def question2(n):
# 	under_r = int(n**(0.5))
# 	xnum = ynum = 0
# 	if under_r**2 == n:
# 		xnum = ynum = 2
# 	i = 1
# 	j = under_r
# 	num = 0
# 	while i <= j:
# 		if i**2 + j**2 == n:
# 			if i != j:
# 				num += 2
# 			else:
# 				num += 1
# 			i += 1
# 		elif i**2 + j**2 < n:
# 			i += 1
# 		else:
# 			j -= 1
# 	return 4*num + xnum + ynum

# # print(question2(1))
# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question2(n))

# def question3(N,M):
# 	if M == N:
# 		return -1
# 	res = [M]*(M+1)
# 	res[N] = 0
# 	for i in range(N+1,M+1):
# 		for k in range(N,i):
# 			if k%(i-k) == 0 and (i-k) != 1 and (i-k) != k:
# 				res[i] = min(res[k]+1,res[i])
# 	if res[-1] >= M:
# 		return -1
# 	else:
# 		return res[-1]


# # print(question3(4,24))
# while 1:
# 	try:
# 		[N,M] = [int(i) for i in input().strip().split()]
# 	except:
# 		break
# 	print(question3(N,M))


# import itertools
  
# def foo():
#     dp = [x for x in itertools.repeat(-1, M * 3 / 2)]
#     T = [[] for x in itertools.repeat(None, M)]
#     dp[M] = 0
#     i = (M - 1) / 2
#     while i > 1:
#         j = i * 2
#         while j < M:
#             T[j].append(i)
#             j += i
#         i -= 1
#     i = M - 1
#     while i >= N:
#         for k in T[i]:
#             v = dp[i + k] + 1
#             if v == 0:
#                 continue
#             if dp[i] == -1:
#                 dp[i] = v
#             elif v < dp[i]:
#                 dp[i] = v
#         i -= 1
#     return dp[N]
    
# while True:
#     try:
#         (N, M) = (int(x) for x in raw_input().split())
#         print foo()
#     except EOFError:
#         break

# def question5(x,y):
# 	rev_x = int(str(x)[::-1])
# 	rev_y = int(str(y)[::-1])
# 	rev_revxy = int(str(rev_x+rev_y)[::-1])
# 	return rev_revxy

# # print(question5(123,100))
# while 1:
# 	try:
# 		x,y = [int(i) for i in input().strip().split()]
# 	except:
# 		break
# 	print(question5(x,y))

# def question6(n):
# 	lst = []
# 	for i in range(1,n+1):
# 		lst.append(findmaxyue(i))
# 	return sum(lst)

# def findmaxyue(n):
# 	res = 0
# 	for i in range(1,n//2+1):
# 		if n%i == 0 and (n/i)%2 == 1:
# 			res = int(n/i)
# 			break
# 	if res == 0:
# 		res = 1
# 	return res

# def question66(n):
# 	if n == 1:
# 		return 1
# 	return sum(list(range(1,n+1,2)))+question66(n//2)

# # # print(findmaxyue(7))
# # print(question6(7))
# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question66(n))

# def question7(n):
# 	i = n//8
# 	last = n%8
# 	while i >= 0:
# 		if last%6 == 0:
# 			j = int(last/6)
# 			return j+i
# 		i -= 1
# 		last += 8
# 	return -1

# while 1:
# 	try:
# 		n = int(input().strip())
# 	except:
# 		break
# 	print(question7(n))

def question8(lst):
	if (lst[0]+lst[2])%2 == 0 and (lst[0]+lst[2])/2 >= 0:
		A = int((lst[0]+lst[2])/2)
	else:
		return 'No'
	if A-lst[0] >= 0:
		B = A-lst[0]
	else:
		return 'No'
	if B-lst[1] >= 0:
		C = B-lst[1]
	else:
		return 'No'
	if B+C == lst[3]:
		return [A,B,C]
	else:
		return 'No'

while 1:
	try:
		lst = [int(i) for i in input().strip().split()]
	except:
		break
	res = question8(lst)
	if res == 'No':
		print('No')
	else:
		print(str(res)[1:-1].replace(',',''))