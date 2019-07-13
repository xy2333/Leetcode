def question(n):
	if n == 0 or n ==1:
		return 
	res = []
	i,rest = rec(n)	
	res.append(i)
	while rest != 1:
		i,rest = rec(rest)
		res.append(i)
	return res

def rec(n):
	pass
	if n == 0:
		return 0
	if n == 1:
		return None,None
	for i in range(2,n+1):
		if n%i == 0:
			rest = int(n/i)
			return i,rest

print(question(1482))