# def num1(n):
# 	num = 0
# 	while n != 0:
# 		n = n&(n-1)
# 		num += 1
# 	return num

# def question1(n,lst):
# 	d = set()
# 	for i in range(len(lst)):
# 		num = num1(lst[i])
# 		d.add(num)
# 	return len(d)

# # n = 5
# # lst = [8,3,5,7,2]
# # print(question1(n,lst))


# while 1:
# 	try:
# 		m = int(input())
# 		for i in range(m):
# 			n = int(input())
# 			lst = [int(i) for i in input().strip().split()]
# 			print(question1(n,lst))
# 	except:
# 		break

# def question2(m,t,m1,t1,m2,t2):
# 	dp = [0]*(t+1)
# 	flag1 = 1
# 	flag2 = 1
# 	for i in range(1,t+1):
# 		temp = dp[i-1] + m1*flag1 - m2*flag2
# 		dp[i] = max(min(temp,m),0)
# 		if i%t1 == 0:
# 			if flag1 == 1:
# 				flag1 = 0
# 			else:
# 				flag1 = 1
# 		if i%t2 == 0:
# 			if flag2 == 1:
# 				flag2 = 0
# 			else:
# 				flag2 = 1
# 	return dp[-1]



# # print(question2(100,100,3,4,4,3))


# while 1:
# 	try:
# 		n = int(input())
# 		for i in range(n):
# 			m,t,m1,t1,m2,t2 = [int(i) for i in input().strip().split()]
# 			print(question2(m,t,m1,t1,m2,t2))
# 	except:
# 		break

def question3(s):
	begin = 0
	end = 0
	count = 0
	length = 0
	while end < len(s):
		if s[end] != 'N':
			count += 1
		end += 1
		while count > 2:
			if s[begin] != 'N':
				count -= 1
			begin += 1
		length = max(length,end-begin)
	return length




# print(question3('NGNNNNGNNNNNNNNSNNNN'))


while 1:
	try:
		n = int(input())
		for i in range(n):
			s = input().strip()
			print(question3(s))
	except:
		break
