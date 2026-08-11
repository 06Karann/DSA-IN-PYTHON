class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        add = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                add += nums[i]
            else:
                break    
        num_set = set(nums)

        while add  in num_set:
            add+=1
        return add        