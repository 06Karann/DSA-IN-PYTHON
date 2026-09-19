class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        window_diff = []
        for i in range(len(nums)-k+1):
            window_diff.append(nums[i+k-1]- nums[i])
        return min(window_diff)   



