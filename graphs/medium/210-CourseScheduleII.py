class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        top = []

        # adj list
        courseToPreq = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            courseToPreq[course].append(preq)

        indegrees = {i: 0 for i in range(numCourses)}
        for course in courseToPreq:
            for neighbor in courseToPreq[course]:
                indegrees[neighbor] += 1
        
        no_incoming_edges = []
        for course in indegrees:
            if indegrees[course] == 0:
                no_incoming_edges.append(course)
        
        while len(no_incoming_edges) > 0:
            deleted = no_incoming_edges.pop()
            top.append(deleted)

            for neighbor in courseToPreq[deleted]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    no_incoming_edges.append(neighbor)


        return top[::-1] if len(top) == len(courseToPreq) else []