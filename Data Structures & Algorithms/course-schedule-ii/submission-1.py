class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = collections.defaultdict(list)
        cycle = set()
        visited = set()
        output = []

        for prereq in prerequisites:
            prereqMap[prereq[0]].append(prereq[1])

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            prereqs = prereqMap[course]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
