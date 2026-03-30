class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        visited = set()
        adjlist = {}
        for course,prereq in prerequisites:
            if course in adjlist:
                adjlist[course].append(prereq)
            else:
                adjlist[course] = [prereq]
        

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for neighbor in adjlist.get(course, []):
                if not dfs(neighbor):
                    return False
            path.remove(course)
            visited.add(course)
            return True
        






        for key in adjlist:
            if not dfs(key):
                return False
        return True