class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        current_sum = 0
        result = 0
        for num in nums:
            current_sum += num

            diff = (current_sum -k)
            if diff in count:
                result += count[diff]
            
            if current_sum in count:
                count[current_sum] += 1
            else:
                count[current_sum] = 1
        
        return result