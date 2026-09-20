class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            rev_pos = 26 - (ord(s[i]) - ord('a'))

            ans+= rev_pos*(i+1)
        
        return ans