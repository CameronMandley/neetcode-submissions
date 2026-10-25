class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        curr_nums = set()
        left = 0
        right = 0
        curr_max = 0
        while right < len(s):
            if s[right] in curr_nums:
                curr_nums.remove(s[left])
                left += 1
            else:
                curr_nums.add(s[right])
                right += 1
                curr_max = max(curr_max, right - left)
        return curr_max
