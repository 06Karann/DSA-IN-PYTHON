class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            need = target - numbers[i]

            low = i+1
            high = len(numbers)-1

            while low<=high:
                mid = (low+high)//2

                if numbers[mid]==need:
                    return [i+1, mid+1]
                elif numbers[mid]<need:
                    low = mid+1
                else:
                    high = mid-1
        return []