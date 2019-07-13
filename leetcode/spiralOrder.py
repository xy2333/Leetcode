class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0:
			return []
		res = []
		while len(matrix[0]) != 0:
			res += matrix[0]
			matrix.pop(0)
			if len(matrix) == 0:
				matrix = [[]]
			else:
				lst = []
				for i in range(len(matrix[0])-1,-1,-1):
					temp = [j[i] for j in matrix]
					lst.append(list(temp))
				matrix = list(lst)
		return res


t = Solution()
s = [[1,2,3],[4,5,6],[7,8,9]]

res = t.spiralOrder(s)
print(res)