class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n==2 or n==3:
            return n
        prev1=2
        prev2=3
        curr=0 
        for i in range(4,n+1):
            curr = prev1+prev2
            prev1=prev2
            prev2 = curr
        return curr    