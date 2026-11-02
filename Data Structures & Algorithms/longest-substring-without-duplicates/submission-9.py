class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsSeen = set()
        longest = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in charsSeen:
                charsSeen.add(s[right])
                longest = max(longest, len(charsSeen))
                right += 1
            else:
                while s[right] in charsSeen and left < right:
                    charsSeen.discard(s[left])
                    left += 1
        return longest
            
        