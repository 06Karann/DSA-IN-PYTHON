class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        left = 0
        product = 1
        total_count = 0

        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            total_count += (right-left+1)
        
        return total_count
     