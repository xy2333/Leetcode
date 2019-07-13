def question(n,h,lst):
	res = [0]*n
	for i in range(n):
		k = (lst[i]-h)/(i+1)
		for j in range(i):
			if lst[j] >= k*(j+1)+h:
				res[i] = j+1
	return res

# lst = [5,4,3,4,3,3,3,3,3]
# print(question(9,5,lst))
while 1:
    try:
        lst1 = [int(i) for i in input().strip().split()]
        lst2 = [int(i) for i in input().strip().split()]
    except:
        break
    a = question(lst1[0],lst1[1],lst2)
    for j in a:
        print(j)



# def question3(k,n,begin,lst):
# 	if k == 0:
# 		return
# 	temp = []
# 	for i in range(begin,n):
# 		if lst[i] > lst[begin] and (i - bgein) <= k:
# 			temp.append(i)
# 	if temp == []:
# 		return question3(k,n,begin+1,lst)
# 	else:
# 		a = 0
# 		index = 0
# 		for j in temp:
# 			if lst[j] > a:
# 				index = j
# 				a = lst[j]
# 		lst[begin],lst[index] = lst[index],lst[begin]
# 		k = k-index
# 		return question3(k,n,begin+1,slt)

# # def Max(lst1,lst2):
# 	# for i in range(len(lst1)):
# 	# 	if lst1[i] > lst2[i]:
# 	# 		return lst1
# 	# 	elif lst1[i]:
# 	# 		lst1[i] < lst2[i]:
# 	# 		return lst2
# 	# return lst1

# lst = [4,2,1,3,5]
# question3(1,5,0,lst)
# print(lst)