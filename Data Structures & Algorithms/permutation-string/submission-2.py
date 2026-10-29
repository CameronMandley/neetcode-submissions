class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def build_dict(s):
            d = {}
            for char in s:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1
            return d
        
        left, right = 0, len(s1)
        s1_dict, s2_dict = build_dict(s1), build_dict(s2[:right])

        while right < len(s2):
            if s1_dict == s2_dict:
                return True
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] == 0:
                s2_dict.pop(s2[left])
            left += 1
            s2_dict[s2[right]] = 1 + s2_dict.get(s2[right], 0)
            right = right + 1
        return s1_dict == s2_dict

        