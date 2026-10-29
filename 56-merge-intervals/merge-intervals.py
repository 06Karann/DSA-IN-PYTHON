class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            last_merged = merged[-1]

            if interval[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], interval[1])
            
            else:
                merged.append(interval)

        return merged