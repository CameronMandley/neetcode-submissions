class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chardict = {}
        for char in s:
            chardict[char] = 1 + chardict.get(char, 0)
        for char in t:
            if char not in chardict or chardict[char] == 0:
                return False
            else:
                chardict[char] -= 1
        return sum(chardict.values()) == 0