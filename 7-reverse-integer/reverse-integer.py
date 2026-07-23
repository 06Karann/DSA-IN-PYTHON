class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX= -2**31, 2**31-1
        # for -ve
        sign=-1
        if x<0:
            x=abs(x)
        else:
            sign=1
        res =0
        while x!=0:
            digit = x%10
            x //= 10
            # overflow condn
            if res > (INT_MAX - digit)//10:
                return 0
            res = res*10+digit
        return sign*res     

