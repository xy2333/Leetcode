class Solution:
	def trap(self, height):
		maxleft = 0
		maxright = 0
		i = 0
		j = len(height)-1
		res = 0
		while i <j:
			if height[i] < height[j]:
				if height[i] > maxleft:
					maxleft = height[i]
				else:
					res += maxleft-height[i]
				i += 1
			else:
				if height[j] > maxright:
					maxright = height[j]
				else:
					res += maxright-height[j]
				j -= 1
		return res




        

        
s = [0,1,0,2,1,0,1,3,2,1,2,1]
t = Solution()
print(t.trap(s))