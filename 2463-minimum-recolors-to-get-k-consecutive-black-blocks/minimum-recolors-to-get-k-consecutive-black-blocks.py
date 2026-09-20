class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        black_block = []

        for i in range(len(blocks)-k+1):
            black_block.append((blocks[i:i+k].count('W')))
              
        return min(black_block)
        