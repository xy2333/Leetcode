class Solution:
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		global maxArea
		maxArea = 0
		def dp(height):
			global maxArea
			if len(height) < 2:
				return maxArea
			if height[0] > height[-1]:
				area = (len(height)-1)*height[-1]
				maxArea = max(maxArea,area)
				height.pop(-1)
			else:
				area = (len(height)-1)*height[0]
				height.pop(0)
			maxArea = max(maxArea,area)
			return dp(height)

		return dp(height)

	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		def dp(height,maxarea):
			if len(height) < 2:
				return maxarea
			else:
				area = (len(height)-1)*min(height[0],height[-1])
				maxarea = max(area,maxarea)
			if height[0] < height[-1]:
				return dp(height[1:],maxarea)
			else:
				return dp(height[:-1],maxarea)

		return dp(height,0)




s = [1,8,6,2,5,4,8,3,7]
t = Solution()
a=t.maxArea(s)
print(a)