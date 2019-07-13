class Solution:
	def ladderLength(self, beginWord, endWord, wordList):
		import collections
		grape = collections.defaultdict(list)
		for word in wordList:
			for i in range(len(word)):
				grape[word[:i]+'#'+word[i+1:]].append(word)
		queue = []
		queue.append((beginWord,1))
		visit = set()
		while len(queue) != 0:
			temp = queue.pop(0)
			if temp[0] == endWord:
				return temp[1]
			visit.add(temp[0])
			for i in range(len(temp[0])):
				for x in grape[temp[0][:i]+'#'+temp[0][i+1:]]:
					if x not in visit:
						visit.add(x)
						queue.append((x,temp[1]+1))
		return 0
        


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
t = Solution()
print(t.ladderLength(beginWord, endWord, wordList))
