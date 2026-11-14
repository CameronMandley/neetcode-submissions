class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = collections.defaultdict(list)
        visited, cycle = set(), set()
        output = []

        for prereq in prerequisites:
            prereqMap[prereq[0]].append(prereq[1])

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in prereqMap[course]:
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
            