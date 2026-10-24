class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen:
                return [seen[rem], i]
            seen[nums[i]] = i
