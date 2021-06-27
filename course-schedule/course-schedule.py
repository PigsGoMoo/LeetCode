class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make a graph
        # Slowly remove prereqs as you take course
        # If no prereqs, add course to stack. 
        # If courses taken == numCourses, return true
        
        graph = collections.defaultdict(list)
        pre = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            pre[prereq].append(course)
            
        stack = []
        
        for i in range(numCourses):
            if not graph[i]:
                stack.append(i)
                
        courses_taken = 0
    
        # Edge case
        if not prerequisites or not numCourses:
            return True
        
        while stack:
            curr_course = stack.pop()
            
            courses_taken += 1
            
            for course in pre[curr_course]:
                graph[course].remove(curr_course)
                if not graph[course]:
                    stack.append(course)
                    
        return courses_taken == numCourses
            