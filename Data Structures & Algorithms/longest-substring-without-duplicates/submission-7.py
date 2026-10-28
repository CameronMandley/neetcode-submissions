class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()
        longest_substring = 0
        left = 0
        for right in range(len(s)):
            while s[right] in curr_chars:
                curr_chars.remove(s[left])
                left += 1
            curr_chars.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring


        