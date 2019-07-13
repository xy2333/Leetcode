class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		import collections
		d = collections.defaultdict(list)
		for x in strs:
			d[tuple(sorted(x))].append(x)
		return list(d.values())
        

s = ["eat", "tea", "tan", "ate", "nat", "bat"]

t = Solution()
res = t.groupAnagrams(s)
print(res)
