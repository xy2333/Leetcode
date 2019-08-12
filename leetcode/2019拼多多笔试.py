# def question1(lst1,lst2):
# 	if len(lst1) == 0 or len(lst2) == 0:
# 		return 'NO'
# 	for i in range(len(lst1)-1):
# 		if lst1[i] >= lst1[i+1]:
# 			index = i+1
# 	res = []
# 	for j in range(len(lst2)):
# 		if (index-1 < 0 or lst2[j] > lst1[index-1]) and (index+1 >= len(lst1) or lst2[j] < lst1[index+1]):
# 			res.append(lst2[j])
# 	if len(res) == 0:
# 		return 'NO'
# 	else:
# 		res.sort()
# 		lst1[index] = res[-1]
# 		return ' '.join([str(x) for x in lst1])

# # lst1 = [int(i) for i in input().strip().split()]
# # lst2 = [int(i) for i in input().strip().split()]
# # print(question1(lst1,lst2))


# # while 1:
# # 	try:
# # 		lst1 = [int(i) for i in input().strip().split()]
# # 		lst2 = [int(i) for i in input().strip().split()]
# # 		print(question1(lst1,lst2))
# # 	except:
# # 		break


def question2(lst):
	for i in range(len(lst)):
		# if len(lst1) >= 2:
			# lst[i] = lst[i][0]+lst[i][-1]
		lst[i] = lst[i][0]+lst[i][-1]

	return rec(lst)

def rec(lst):
	if len(lst) == 1:
		if lst[0][0] == lst[0][-1]:
			return 'true'
		else:
			return 'false'
	else:
		for i in range(1,len(lst)):
			if lst[i][0] == lst[0][-1]:
				lst[0] = lst[0][0]+lst[i][-1]
				lst.pop(i)
				return rec(lst)
			elif lst[i][-1] == lst[0][0]:
				lst[0] = lst[i][0] +lst[0][-1]
				lst.pop(i)
				return rec(lst)

		return 'false'

# lst = input().strip().split()
lst = ['C','TIGER','RPC']
# lst = ['CAT','RPC']

print(question2(lst))


# while 1:
# 	try:
# 		lst = input().strip().split()
# 		# lst = ['CAT','TIGER','RPC']
# 		# lst = ['CAT','RPC']

# 		print(question2(lst))
# 	except:
# 		break

# def question4(length,weight):
# 	dp = [([],[]) for i in range(len(length))]
# 	dp[0] = ([length[0]],[weight[0]])
# 	for i in range(1,len(length)):
# 		if length[i] <= dp[i-1][0][-1]:
# 			dp[i] = dp[i-1]
# 			if len(dp[i-1][0])>= 2 and length[i] > dp[i-1][0][-2] and weight[i] < dp[i-1][1][-1]:
# 				dp[i] = (dp[i][0][:-1]+[length[i]],dp[i][1][:-1]+[weight[i]])
# 				pass
# 		else:
# 			if weight[i]*7 >= sum(dp[i-1][1]):
# 				dp[i] = (dp[i-1][0]+[length[i]],dp[i-1][1]+[weight[i]])
# 			else:
# 				dp[i] = dp[i-1]

				
# 			# else:
# 				# if sum(dp[i-1][1][1:]):
# 	return len(dp[-1][0])



# # lst = input().strip().split()
# length = [3,4,5,6,7,8,9,10]
# weight = [1,1,1,1,1,1,1,10]

# print(question4(length,weight))


# while 1:
# 	try:
# 		n = int(input())
# 		length = [int(x) for x in input().strip().split()]
# 		weight = [int(x) for x in input().strip().split()]

# 		# lst = ['CAT','TIGER','RPC']
# 		# lst = ['CAT','RPC']
# 		print(question4(length,weight))
# 	except:
# 		break