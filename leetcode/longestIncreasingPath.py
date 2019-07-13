class Solution:
	def longestIncreasingPath(self, matrix):
		try:
			memery = [[None]*len(matrix[0]) for i in range(len(matrix))]
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					res = self.dfs(matrix,memery,i,j)
			return max([max(x) for x in memery])
		except:
			return 0


	def dfs(self,matrix,memery,i,j):
		if memery[i][j] is not None: 
			return memery[i][j]
		lst = [(0,1),(0,-1),(-1,0),(1,0)]
		res = 1
		for step in lst:
			a = i+step[0]
			b = j + step[1]
			if 0 <= a < len(matrix) and 0 <= b < len(matrix[0]) and matrix[i][j] < matrix[a][b]:
				if memery[a][b] is None:
					memery[a][b] = self.dfs(matrix,memery,a,b)
				res = max(res,1+ memery[a][b])
		memery[i][j] = res
		return res



s = [[7,7,5],[2,4,6],[8,2,0]]
t = Solution()
print(t.longestIncreasingPath(s))