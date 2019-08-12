def question1(n,lst):
	import itertools
	row = [i for i in range(1,n+1)]
	temp = list(itertools.permutations(row,n))
	# temp.sort()
	index = temp.index(tuple(lst))
	res = temp[-(index+1)]
	return ' '.join([str(x) for x in res])

# # n = 5
# # lst = [3,1,5,2,4]
# # print(question1(n,lst))

# while 1:
# 	try:
# 		n = int(input())
# 		lst = [int(i) for i in input().strip().split()]
# 		print(question1(n,lst))
# 	except:
# 		break
def findminodd(lst):
	if len(lst) == 0:
		return None,None
	index = minodd = None
	for i in range(len(lst)):
		if lst[i]%2 == 0:
			if minodd is None or minodd > lst[i]:
				minodd = lst[i]
				index = i+1
	return index,minodd

def findmineven(lst):
	if len(lst) == 0:
		return None,None
	index = mineven = None
	for i in range(len(lst)):
		if lst[i]%2 == 1:
			if mineven is None or mineven > lst[i]:
				mineven = lst[i]
				index = i+1
	return index,mineven

def question3(lst):
	if len(lst) == 0:
		return []
	if lst[0]%2 == 1:
		index,minodd = findminodd(lst[1:])
		if minodd is not None and minodd < lst[0]:
			lst[0],lst[index] = lst[index],lst[0]
			index,mineven = findmineven(lst[1:])
			if mineven is not None and mineven < lst[0]:
				lst[0],lst[index] = lst[index],lst[0]
		return [lst[0]]+question3(lst[1:])
	else:
		index,mineven = findmineven(lst[1:])
		if mineven is not None and mineven < lst[0]:
			lst[0],lst[index] = lst[index],lst[0]
			index,minodd = findminodd(lst[1:])
			if minodd is not None and minodd < lst[0]:
				lst[0],lst[index] = lst[index],lst[0]
		return [lst[0]]+question3(lst[1:])

# n = 5
lst = [1,1,1,1]
# lst = [53941,38641,31525,75864,29026,12199,83522,58200,64784,80987]

print(question3(lst))

# while 1:
# 	try:
# 		n = int(input())
# 		lst = [int(i) for i in input().strip().split()]
# 		res = question3(lst)
# 		print(' '.join([str(x) for x in res]))
# 	except:
# 		break




while 1:
	try:
		n = int(input().strip())
		lst = [int(i) for i in input().strip().split()]
		lst = [int(i) for i in input().strip().split()]

		# res = question3(lst)
		for i in range(n):
			print('YES')
		# print(' '.join([str(x) for x in res]))
	except:
		break


while 1:
	try:
		n = int(input().strip())
		for i in range(n):
			lst = [int(i) for i in input().strip().split()]
			lst = [int(i) for i in input().strip().split()]

		# res = question3(lst)
		for i in range(n):
			print('NO')
		# print(' '.join([str(x) for x in res]))
	except:
		break