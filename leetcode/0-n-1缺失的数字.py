def find(lst):
	def binaryfind(lst,begin,end):
		if begin>=end:
			return end
		index = (end-begin)//2+begin
		if lst[index] != index and (index-1 < begin or lst[index-1] ==  index-1):
			return index
		if lst[index] == index:
			return binaryfind(lst,index+1,end)
		else:
			return binaryfind(lst,begin,index)

	return binaryfind(lst,0,len(lst))

print(find([0]))