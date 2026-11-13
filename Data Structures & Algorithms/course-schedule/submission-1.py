class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = collections.defaultdict(list)
        visited = set()

        for prereq in prerequisites:
            prerequisiteMap[prereq[0]].append(prereq[1])

        def dfs(course):
            if course in visited:
                return False
            if prerequisiteMap[course] == []:
                return True
            visited.add(course)
            prereqs = prerequisiteMap[course]
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            prerequisiteMap[course] = []
            return True    

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

        