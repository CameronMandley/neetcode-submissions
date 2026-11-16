class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for from_i, to_i, price_i in flights:
            adj[from_i].append((to_i, price_i))
        
        minHeap = [(0, 0, src)]
        best = {(src, 0): 0}

        while minHeap:
            curr_price, curr_stops, source = heapq.heappop(minHeap)
            if curr_price > best[(source, curr_stops)]:
                continue
            if source == dst:
                return curr_price
            for to_i, price_i in adj[source]:
                if curr_stops <= k:
                    new_price = curr_price + price_i
                    new_stops = curr_stops + 1
                    if new_price < best.get((to_i, new_stops), float("inf")):
                        best[(to_i, new_stops)] = new_price
                        heapq.heappush(minHeap, (new_price, new_stops, to_i))
        return -1
        