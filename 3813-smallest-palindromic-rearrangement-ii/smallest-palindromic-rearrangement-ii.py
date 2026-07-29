class Solution:
    def get_combinations(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k > n // 2:
            k = n - k
        
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
            if res > 10**15:
                return 10**15
        return res

    def count_ways(self, freq_list: list) -> int:
        total = sum(freq_list)
        ways = 1
        for count in freq_list:
            if count == 0:
                continue
            ways *= self.get_combinations(total, count)
            total -= count
            if ways > 10**15:
                ways = 10**15
        return ways

        
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        count = Counter(s)
        
        # Check if a palindrome is possible (at most one odd frequency is allowed)
        odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Step 2: Prepare half frequencies in alphabetical order (A-Z)
        half_counts = []
        unique_chars = sorted(count.keys())
        
        for ch in unique_chars:
            half_counts.append(count[ch] // 2)
            
        # Step 3: Check if 'k' is within the total possible permutations
        total_permutations = self.count_ways(half_counts)
        if k > total_permutations:
            return ""
            
        # Step 4: Build the left half character by character (digit-by-digit approach)
        left_half = []
        half_len = sum(half_counts)
        
        for _ in range(half_len):
            for i in range(len(unique_chars)):
                if half_counts[i] == 0:
                    continue
                    
                # Temporarily pick this character
                half_counts[i] -= 1
                ways = self.count_ways(half_counts)
                
                if ways >= k:
                    # If the number of ways covers 'k', lock this character in
                    left_half.append(unique_chars[i])
                    break
                else:
                    # Otherwise, subtract the ways and try the next character
                    k -= ways
                    half_counts[i] += 1
                    
        # Step 5: Assemble and return the final palindrome: left_str + mid_char + reversed(left_str)
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]