class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}

        if len(s1) > len(s2):
            return False

        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)
        for char in s2[:len(s1)]:
            s2_dict[char] = 1 + s2_dict.get(char, 0)

        if s1_dict == s2_dict:
            return True

        left, right = 0, len(s1) - 1

        while right < len(s2) - 1:
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
            left += 1
            right += 1
            s2_dict[s2[right]] = 1 + s2_dict.get(s2[right], 0)
            if s1_dict == s2_dict:
                return True
        return False

        