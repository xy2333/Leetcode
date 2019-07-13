class Solution:
	def numIslands1(self, grid):
		try:
			r = 0
			m = len(grid)
			n = len(grid[0])
		except:
			return 0
		for i in range(m):
			for j in range(n):
				if int(grid[i][j]) == 1:
					r += 1
					grid[i][j] = '0'
					q = []
					q.append((i,j))
					while len(q) != 0:
						temp = q.pop(0)
						for a,b in [(0,1),(1,0),(0,-1),(-1,0)]:
							x = a+temp[0]
							y = b+temp[1]
						if x >= 0 and x < m and y >= 0 and y < n and int(grid[x][y]) == 1 :
							q.append((x,y))
							grid[x][y] = 0
		return r

	def numIslands(self, grid):
		try:
			r = 0
			m = len(grid)
			n = len(grid[0])
		except:
			return 0
		def rec(i,j):
			if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and int(grid[i][j]) == 1:
				grid[i][j] = '0'
				for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
					rec(a+i,b+j)
				return 1
			else:
				return 0
		res = 0
		for i in range(m):
			for j in range(n):
				res += rec(i,j)
		return res





        
        
s = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
t = Solution()
print(t.numIslands(s))