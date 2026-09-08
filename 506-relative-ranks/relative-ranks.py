class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        pair = []

        for i in range(n):
            pair.append([score[i],i])

        pair.sort(reverse=True)
        result =[""]*n
        
        for i in range(n):
            original_index = pair[i][1]
            if i == 0:
                result[original_index] = "Gold Medal"
            elif i == 1:
                result[original_index] = "Silver Medal"
            elif i ==2:
                result[original_index] = "Bronze Medal"
            else:
                result[original_index] = str(i+1)
        return result
        