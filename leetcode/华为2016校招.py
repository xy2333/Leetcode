# def q(lst,begin,end):
# 	if begin <= end:
# 		return max(lst[begin-1:end])
# 	else:
# 		return max(lst[end-1:begin])
# def u(lst,index,score):
# 	lst[index-1] = score

# while 1:
# 	try:
# 		[N,M] =[int(i) for i in input().strip().split()]
# 		lst = [int(i) for i in input().strip().split()]
# 		for j in range(M):
# 			todo = input().strip().split()
# 			if todo[0] == 'Q':
# 				print(q(lst,int(todo[1]),int(todo[2])))
# 			else:
# 				u(lst,int(todo[1]),int(todo[2]))
# 	except:
# 		break

# import collections
# import operator
# def question2(lst):
# 	d = collections.OrderedDict()
# 	for i in lst:
# 		d[i] = d.get(i,0)+1
# 	lsort = sorted(d.items(),key = operator.itemgetter(1),reverse = True)
# 	num = min(8,len(lsort))
# 	res = [[None]*2 for k in range(num)]
# 	for j in range(num):
# 		temp = lsort[j][0].split()
# 		res[j][0] = temp[0][-16:]+' '+temp[1]
# 		res[j][1] = lsort[j][1]
# 	return res

# # lst = ['fpgadrive.c 1325','fpgadrive.c 1325','aaaaaaaaaaaaaaaaaaaf.c 1325','drive.c 1325']
# lst = []
# while 1:
# 	try:
# 		a = input().strip().split('\\')
# 		lst.append(a[-1])
# 	except:
# 		break

# res = question2(lst)
# for i in res:
# 	print(i[0],str(i[1]))

def question(lst1,lst2):
	m1 = match(lst1)
	m2 = match(lst2)
	lst1 = tran(lst1)
	lst2 = tran(lst2)
	if m1 == 'king' or m1 == 'bang' or m2 == 'king' or m2 == 'bang':
		if m1 == 'king':
			return lst1
		if m2 == 'king':
			return lst2
		if m1 == 'bang' and m2 == 'bang':
			if lst1[0] > lst2[0]:
				return lst1
			else:
				return lst2
		else:
			if m1 == 'bang':
				return lst1
			else:
				return lst2
	else:
		if m1 != m2:
			return 'ERROR'
		else:
			if lst1[0] > lst2[0]:
				return lst1
			else:
				return lst2

def match(lst):
	if lst[0] == 'joker':
		return 'king'
	if len(lst) == 3:
		return 'three'
	if len(lst) == 4:
		return 'bang'
	if len(lst) == 2:
		return 'two'
	if len(lst) == 1:
		return 'one'
	if len(lst) == 5:
		return 'five'

def tran(lst):
	d = {'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14,'2':15,'joker':'joker','JOKER':'JOKER'}
	for i in range(len(lst)):
		lst[i] = d[lst[i]]
	return lst

# lst1 = ['4','4','4','4']
# lst2 = ['joker','JOKER']


while 1:
	try:
		s = input().strip().split('-')
		lst1 = s[0].strip().split()
		lst2 = s[1].strip().split()
	except:
		break
	res = question(lst1,lst2)
	if res == 'ERROR':
		print('ERROR')
	else:
		for i in res:
			if i == 11:
				print('J',end = ' ')
			elif i == 12:
				print('Q',end = ' ')
			elif i == 13:
				print('K',end = ' ')
			elif i == 14:
				print('A',end = ' ')
			elif i == 15:
				print(2,end = ' ')
			else:
				print(i,end = ' ')
