def question(lst):
	res = []
	for i in lst:
		res.append(i//2)
	return res

# lst = [3,10,81]
# print(question(lst))

while 1:
	try:
		lst = []
		while 1:
			i = int(input().strip())
			if i != 0:
				lst.append(i)
		res = question(lst)
		for j in res:
			print(j)
	except:
		break

def question3(s):
	ss = s[2:]
	d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
	ls = []
	for i in ss:
		ls.append(d[i])
	res = 0
	for j in range(len(ls)):
		res += ls[-(j+1)]*(16**j)
	return res
# s = '0xA'
# print(question3(s))
while 1:
	try:
		s = input().strip()
	except:
		break
	print(str(question3(s)))

def question2(lst):
	lset = set(lst)
	return sorted(lset)

# lst = [11,10,20,40,32,67,40,20,89,300,400,15]
# res = question2(lst)
while 1:
	try:
		N = int(input().strip())
		lst = []
		for i in range(N):
			num = int(input().strip())
			lst.append(num)
	except:
		break
	res = question2(lst)
	for i in res:
		print(i)