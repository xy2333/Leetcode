class Solution(object):
	def kthSmallest(self, matrix, k):
		"""
		:type matrix: List[List[int]]
		:type k: int
		:rtype: int
		"""
		indexs = [0]*len(matrix)
		for i in range(k):
			minnum = float('inf')
			for j in range(len(indexs)):
				if indexs[j] < len(matrix) and matrix[indexs[j]][j] < minnum:
					minnum = matrix[indexs[j]][j]
					temp = j
			indexs[temp] = indexs[temp]+1
		return minnum
        
        

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]]

t = Solution()
res = t.kthSmallest(matrix,8)
print(res)
