class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            id = ''.join(sorted(string))
            groups[id].append(string)
        return list(groups.values())

        