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
