class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        k_freq = sorted(freq_dict.values())[-k:]
        return [num for num in freq_dict if freq_dict[num] in k_freq]
        