class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        for char in t:
            if char not in letters or letters[char] == 0:
                return False
            else:
                letters[char] -= 1
        return sum(letters.values()) == 0