class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		a = len(nums1)
		b = len(nums2)
		if len(nums1) <= len(nums2):
			lst1 = nums1
			lst2 = nums2
		else:
			lst1 = nums2
			lst2 = nums1
		m = len(lst1)
		n = len(lst2)

		left = 0
		right = m
		while left <= right:
			i = (left+right)//2
			j = (m+n)//2-i
			if (j <= 0 or i == m or lst1[i] >= lst2[j-1]) and (i <= 0 or j ==n or lst1[i-1] <= lst2[j]):
				if (m+n)%2 == 1:
					if i == m:
						return lst2[j]
					elif j == n:
						return lst1[i]
					else:
						return min(lst1[i],lst2[j])
				else:
					if i == m:
						minright = lst2[j]
					elif j == n:
						minright = lst1[i]
					else:
						minright = min(lst1[i],lst2[j])

					if i == 0:
						maxleft = lst2[j-1]
					elif j == 0:
						maxleft = lst1[i-1]
					else:
						maxleft = max(lst1[i-1],lst2[j-1])
					return (maxleft+minright)/2.0

			elif j >= 0 and i < m and lst1[i] < lst2[j-1]:
				left = i+1
			else:
				right = i

        


t = Solution()
nums1 = [1,2]
nums2 = [3,4]

res = t.findMedianSortedArrays(nums1,nums2)
print(res)
