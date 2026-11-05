class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1) - 1
        s1_dict = {}
        s2_dict = {}
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        for char in s2[:len(s1)]:
            if char not in s2_dict:
                s2_dict[char] = 1
            else:
                s2_dict[char] += 1
        
        if s1_dict == s2_dict:
            return True


        while right < len(s2) - 1:
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
            left += 1
            right += 1
            if s2[right] not in s2_dict:
                s2_dict[s2[right]] = 1
            else:
                s2_dict[s2[right]] += 1
            if s1_dict == s2_dict:
                return True
        return False
