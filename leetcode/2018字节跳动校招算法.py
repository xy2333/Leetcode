# def question1(n,lst):
# 	lst.sort(key = lambda x: x[0],reverse = True)
# 	ymax = lst[0][1]-1
# 	res = []
# 	for i in range(n):
# 		if lst[i][1] > ymax:
# 			res.append(lst[i])
# 			ymax = lst[i][1]

# 	return res[::-1]

# # lst = [[1,2],[5,3],[4,6],[7,5],[9,0]]
# while 1:
# 	try:
# 		n = int(input().strip())
# 		lst = []
# 		for i in range(n):
# 			lst.append([int(j) for j in input().strip().split()])
# 	except:
# 		break

# 	res = question1(n,lst)
# 	for i in res:
# 		print(str(i)[1:-1].replace(',',''))

def question2(n,lst):
	maxres = 0
	for i in range(n):
		start = i
		end = i
		while start-1 >= 0 and lst[start-1] >= lst[i]:
			start -= 1
		while end+1 <= n-1 and lst[end+1] >= lst[i]:
			end += 1
		add = sum(lst[start:end+1])
		res = add*lst[i]
		maxres = max(res,maxres)
	return maxres


while 1:
	try:
		n = int(input().strip())
		lst = [int(j) for j in input().strip().split()]

	except:
		break

	print(question2(n,lst))