class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        for course,prereq in prerequisites:
            if course not in adjlist:
                adjlist[course] = [prereq]
            else:
                adjlist[course].append(prereq)
            if prereq not in adjlist:
                adjlist[prereq] = []
               
        seen = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if adjlist[course] == []:
                return True

            path.add(course)
            for pre in adjlist[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            seen.add(course)
            return True
            
        for key in adjlist:
            if not dfs(key):
                return False
        return True
        



        
        




