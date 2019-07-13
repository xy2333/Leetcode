def merge_sort(lst):
	def merge_pass(lfrom,lto,llen,slen):
		i = 0
		while (i+2)*slen <= llen:
			merge(lfrom,lto,i*slen,(i+1)*slen,(i+2)*slen)
			i += 2
		if (i+1)*slen < llen:
			merge(lfrom,lto,i*slen,(i+1)*slen,llen)
		else:
			for j in range(i*slen,llen):
				lto[j] = lfrom[j]

	def merge(lfrom,lto,low,mid,high):
		i = low
		j =	mid 
		k = low
		while i < mid and j < high:
			if lfrom[i] < lfrom[j]:
				lto[k] = lfrom[i]
				k += 1
				i +=1
			else:
				lto[k] = lfrom[j]
				k += 1
				j +=1
		if i >= mid:
			lto[k:high] = lfrom[j:high]
		else:
			lto[k:high] = lfrom[i:mid]

	llen = len(lst)
	temp = [None]*llen
	slen = 1
	while slen < llen:
		merge_pass(lst,temp,llen,slen)
		slen *= 2
		merge_pass(temp,lst,llen,slen)
		slen *= 2
	return lst

s = [6,5,4,3,2,1]
a = merge_sort(s)
print(a)