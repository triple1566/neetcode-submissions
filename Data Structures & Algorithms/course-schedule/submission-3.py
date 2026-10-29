class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])
        # we populated the adjacency list

        # define a set for all nodes currently visiting in our dfs call stream
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if adjList[course]==[]:
                return True
            visiting.add(course)
            for req in adjList[course]:
                if not dfs(req):
                    return False
            visiting.remove(course)
            # CRUCIAL!! This line removes courses known to be completable from the adjacency list, ensuring efficient runtime.
            adjList[course]=[]
            return True

        for course in range(numCourses):
            # check for completability per course
            if not dfs(course):
                return False
        return True