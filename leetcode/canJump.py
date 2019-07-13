class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = 0
        for idx,value in enumerate(nums):
            if length >= len(nums)-1:
                return True
            if idx <= length:
                length = max(length,idx+value)
        return False


        

s = [3,2,1,0,4]
t = Solution()
print(t.canJump(s))
