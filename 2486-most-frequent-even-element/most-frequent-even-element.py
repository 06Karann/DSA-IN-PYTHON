class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        if len(nums)==0: 
            return -1
        even_num  = []    
        for x in nums:
            if x%2==0:
                even_num.append(x)
        if not even_num:
            return -1
        freq = Counter(even_num) 
        max_freq = -1
        result = -1
        for num, count in freq.items():
            if count > max_freq or (count == max_freq and num < result):
                max_freq = count
                result = num
        return result        
