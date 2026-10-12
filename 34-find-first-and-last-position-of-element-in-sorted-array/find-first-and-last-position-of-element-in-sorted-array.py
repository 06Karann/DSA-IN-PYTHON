class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(nums,target,is_first):
            low = 0
            high = len(nums)-1
            result = -1
            while low <= high:
                mid = (low+high)//2

                if nums[mid] == target:
                    result = mid
                    if is_first:
                        high = mid-1
                    else:
                        low = mid+1
                elif nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return result
        
        first = binary_search(nums,target,True)
        last = binary_search(nums,target,False)

        return [first, last]