class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        freq = Counter(nums)

        for num, count in freq.items():
            if count > n//3:
                ans.append(num)
        return ans        