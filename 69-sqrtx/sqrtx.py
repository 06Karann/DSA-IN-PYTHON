class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = 0
        if x==0:
            return 0
        
        while low <= high:
            mid = (low+high)//2

            if (mid*mid)<=x:
                low = mid+1
                ans = mid
            else:
                high = mid-1
        return ans