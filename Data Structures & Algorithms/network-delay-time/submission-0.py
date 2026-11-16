class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        visit = set()
        for source, target, time in times:
            adj[source].append((target, time))
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            time, source = heapq.heappop(minHeap)
            if source in visit:
                continue
            visit.add(source)
            t = max(time, t)
            for target_node, target_time in adj[source]:
                if target_node not in visit:
                    heapq.heappush(minHeap, (target_time + time, target_node))
        return t if len(visit) == n else -1
                
        