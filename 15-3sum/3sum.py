class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            fixed = nums[i]
            left = i+1
            right = len(nums) - 1

            while left<right:
                
                if fixed + nums[left] + nums[right]==0:
                    result.append([fixed, nums[left], nums[right]])
                    left += 1
                    right -= 1 

                    # Duplicate
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif fixed + nums[left] + nums[right]<0:  
                    left+=1
                else:
                    right-=1 

        return result            