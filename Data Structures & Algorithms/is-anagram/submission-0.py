class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for c in s:
            if c not in dictionary:
                dictionary[c] = 1
            else:
                dictionary[c] += 1
        for c in t:
            if c not in dictionary:
                return False
            else:
                dictionary[c] -= 1
                if dictionary[c] < 0:
                    return False
        print(dictionary)
        return max(dictionary.values()) == 0
        