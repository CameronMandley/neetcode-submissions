class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        for char in t:
            if char not in chars or chars[char] == 0:
                return False
            else:
                chars[char] -= 1
        return sum(chars.values()) == 0
        