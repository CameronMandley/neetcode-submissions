class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = collections.defaultdict(list)
        visited = set()

        for prereq in prerequisites:
            prerequisiteMap[prereq[0]].append(prereq[1])


        def dfs(i):
            if i in visited:
                return False
            if prerequisiteMap[i] == []:
                return True
            visited.add(i)
            prereqs = prerequisiteMap[i]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visited.remove(i)
            prerequisiteMap[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        