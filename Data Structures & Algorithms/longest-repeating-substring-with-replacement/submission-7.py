class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0
        most_freq = 0
        seen = {}

        while right < len(s):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1
            most_freq = max(most_freq, seen[s[right]])  
            while ((right - left + 1) - most_freq > k) and left < right:
                    seen[s[left]] -= 1
                    left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
