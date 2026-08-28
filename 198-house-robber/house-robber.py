class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # Initialize DP array
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill DP array
        for i in range(2, n):
            # Either don't rob current house (take previous max)
            # or rob current house + max from two houses back
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
        return dp[n-1]