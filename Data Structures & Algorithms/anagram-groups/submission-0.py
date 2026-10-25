class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            string2 = "".join(sorted(string))
            if string2 in anagrams:
                anagrams[string2] += [string]
            else:
                anagrams[string2] = [string]
        return[value for value in anagrams.values()]
        