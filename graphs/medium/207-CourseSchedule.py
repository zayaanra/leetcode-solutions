class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courseToPreq = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            courseToPreq[course].append(preq)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if courseToPreq[course] == []:
                return True
            
            visited.add(course)
            for preq in courseToPreq[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            courseToPreq[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True