class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in nums:
                j=nums.index(temp)
                if(i==j):
                    continue
                else:
                    return [i,j]

