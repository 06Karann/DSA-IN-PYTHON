class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=1                    
            else:
                dict[s[i]]+=1 
        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
            
        return -1      