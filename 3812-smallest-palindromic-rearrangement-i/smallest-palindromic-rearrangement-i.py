class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.keys())
        left_half = []
        middle_char = ""
        for char in sorted_chars:
            freq = count[char]
            if freq % 2 != 0:
                middle_char = char
            left_half.append(char * (freq // 2))
        left_str = "".join(left_half)    
        return left_str + middle_char + left_str[::-1]    