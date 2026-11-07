class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) - 1
        freqs = [(freq_dict[num], num) for num in freq_dict]
        heapq.heapify(freqs)
        results = []
        for i in range(k):
            results += [heapq.heappop(freqs)[1]]
        return results
        