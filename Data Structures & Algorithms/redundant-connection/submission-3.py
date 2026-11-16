class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for nodei, nodej in edges:
            root_i = find(nodei)
            root_j = find(nodej)
            if root_i == root_j:
                return [nodei, nodej]
            parent[root_i] = root_j
