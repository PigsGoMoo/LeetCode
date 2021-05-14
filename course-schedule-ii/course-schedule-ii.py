class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # We can solve this by making a graph of prereqs to courses
        # If we take a prereq course, the next course won't have a prereq
        # So we just make the map and whichever is empty (aka has no more prereqs)
        # can be taken next
        
        # Initialize and make our graph. The key will be the prereq and the value is the
        # list of courses it unlocks
        prereqs = collections.defaultdict(list)
        # Also keep track of how many prereqs a course has
        prereq_count = {}
        
        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
            prereq_count[course] = prereq_count.get(course, 0) + 1
        
        
        queue = collections.deque()
        # Iterate through courses, adding them to queue if they have no prereq 
        # We can tell that they have no prereq because they won't be in prereq_count
        for i in range(numCourses):
            if i not in prereq_count:
                queue.append(i)
                
        ans = []
        # Now we go through the queue and remove it from the prereqs and then lower the count
        # of the courses that have it as a prereq
        while queue:
            # Grab the course
            course = queue.popleft()
            # Add to ans
            ans.append(course)
            # Remove from prereqs
            for next_step in prereqs[course]:
                # Detract from prereq count
                prereq_count[next_step] -= 1
                # If no more prereqs, add to queue
                if prereq_count[next_step] == 0:
                    queue.append(next_step)
        # If there's a cycle in our prereqs, the length of ans won't equal the number of courses.
        return ans if len(ans) == numCourses else []
            