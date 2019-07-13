class Solution:
    # def twoSum(self, nums, target):
    #     nums = tuple(nums)
    #     lens = len(nums)
    #     lists = list(range(lens))
    #     for num in nums:
    #         if target-num in nums :
    #             if num == target-num:
    #                 newnums = list(nums)
    #                 newnums.remove(num)
    #                 if target-num in newnums :
    #                     return [nums.index(num),newnums.index(target-num)+1]
    #             else:
    #                 return [nums.index(num),nums.index(target-num)]
   
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in nums and nums.index(diff) != i:
        #         # nums[i] = float('nan')
        #         return [i, nums.index(diff)]
        size = len(nums)
        for i in range(size-1):
            for j in range(i+1,size):
                if nums[i]+nums[j] == target:
                    return [i,j]

			

nums = [3,3]
target = 6
s = Solution()
ans=s.twoSum(nums,target)
print(ans)

