class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        output = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                output = max(output, r - l + 1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                charSet.add(s[r])
                output = max(output, r - l + 1)
        return output
            
        