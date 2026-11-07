class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)
        heap = []
        for num in num_dict.keys():
            heapq.heappush(heap, (num_dict[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res += [heapq.heappop(heap)[1]]
        return res
        