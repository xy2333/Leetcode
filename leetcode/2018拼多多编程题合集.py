# def question4(hp,n,b):
# 	if 2*n >= b:
# 		res = hp//n
# 		if hp%n == 0:
# 			return res
# 		else:
# 			return res+1
# 	else:
# 		res = hp//b
# 		res *= 2
# 		if hp%b == 0:
# 			return res
# 		elif hp-res*b/2 <= n:
# 			return res +1
# 		else:
# 			return res+2

# while 1:
# 	try:
# 		hp = int(input())
# 		n = int(input())
# 		b = int(input())
# 		print(question4(hp,n,b))
# 	except:
# 		break

# def question1(n,k,s):
# 	d = Counter(s)
# 	minres = ['9']*n
# 	minres = ''.join(minres)
# 	mincost = float('inf')
# 	for i in range(10):
# 		need = k - d[str(i)]
# 		if need <= 0:
# 			res = s
# 			cost = 0
# 		else:
# 			res = s
# 			gap = 1
# 			cost = 0
# 			while need > 0:
# 				if i+gap <= 9:
# 					if d[str(i+gap)] >= need:
# 						res = res.replace(str(i+gap),str(i),need)
# 						cost += need*gap
# 						need = 0
# 					else:
# 						res = res.replace(str(i+gap),str(i))
# 						need = need-d[str(i+gap)]
# 						cost += d[str(i+gap)]*gap
# 				if need == 0:
# 					break
# 				else:
# 					if i-gap >= 0:
# 						if d[str(i-gap)] >= need:
# 							res = res[::-1]
# 							res = res.replace(str(i-gap),str(i),need)
# 							res = res[::-1]
# 							cost += need*gap
# 							need = 0
# 						else:
# 							res = res.replace(str(i-gap),str(i))
# 							need = need-d[str(i-gap)]
# 							cost += d[str(i-gap)]*gap
# 				gap += 1
# 		if cost < mincost:
# 			mincost = cost
# 			minres = res
# 		elif cost == mincost:
# 			minres = min(minres,res)
# 	return mincost,minres


# from collections import Counter
# while 1:
# 	try:
# 		n,k = [int(i) for i in input().strip().split()]
# 		s = input()
# 		res = question1(n,k,s)
# 		print(res[0])
# 		print(res[1])
# 	except:
# 		break

# def question3(n,lst):
# 	lst.sort()
# 	sums = []
# 	for i in range(n//2):
# 		sums.append(lst[i]+lst[-(i+1)])
# 	sums.sort()
# 	return sums[-1]-sums[0]

# while 1:
# 	try:
# 		n = int(input())
# 		lst = [int(i) for i in input().strip().split()]
# 		print(question3(n,lst))
# 	except:
# 		break
def isture(d):
	num = 0
	for i in d:
		num += d[i]
	for i in d:
		if d[i] > num//2:
			return i
	return 0
def question2(n,lst):
	d = {}
	for i in range(1,n+1):
		d[i] = lst[i-1]
	index = isture(d)
	if index != 0 and d[index]*2-1 > sum(lst):
		return '-'
	res = []
	while len(d) != 0:
		index = isture(d)
		if index == 0:
			for i in range(1,n+1):
				if i in d and (len(res) == 0 or res[-1] != i):
					res.append(i)
					d[i] -= 1
					if d[i] == 0:
						d.pop(i)
					break
		else:
			res.append(index)
			d[index] -= 1
			if d[index] == 0:
				d.pop(index)
	return ' '.join([str(x) for x in res])
while 1:
	try:
		n = int(input())
		lst = [int(i) for i in input().strip().split()]
		print(question2(n,lst))
	except:
		break

