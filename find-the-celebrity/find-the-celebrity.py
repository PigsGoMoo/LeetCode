# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Make a graph
        # The one with an in-degree of n-2 is the answer
        # Need to use knows to see whether or not there's a connection
#         # Too slow        
#         graph = collections.defaultdict(list)
#         indegree = collections.defaultdict(int)
#         most_known = 0
#         num_known = 0
        
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if knows(i, j):
#                     graph[i].append(j)
#                     indegree[j] += 1
#                     if indegree[j] > num_known:
#                         num_known = indegree[j]
#                         most_known = j

#                 if knows(j, i):
#                     graph[j].append(i)
#                     indegree[i] += 1
#                     if indegree[i] > num_known:
#                         num_known = indegree[i]
#                         most_known = i
        
#         # print(graph)
#         # print(indegree)
        
#         if num_known == n-1 and not graph[most_known]:
#             return most_known
            
#         return -1

        def is_celebrity(n, celeb):
            counter = 0
            # print("Checking if celeb {} is valid. n: {}".format(celeb, n))
            for i in range(n):
                if i == celeb:
                    continue
                
                if knows(i, celeb):
                    # print("{} knows him, so +1".format(i))
                    counter += 1
                else:
                    # print("{} doesn't know him. Not a celeb".format(i))
                    return False
                
                if knows(celeb,i):
                    # print("Celeb knows {}, it's not him".format(i))
                    return False
                
            return counter == n - 1
            
            

        # Keep an array of candidates and make a graph. 
        candidate = [i for i in range(n)]
        
        # We'll start at the beginning and move to the left any that is disqualified
        # We can disqualify based on two scenarios
        # if know(a,b) is True, then we know that a cannot be the celebrity because it knows someone
        # if know(a,b) is False, then we know that b cannot be the celebrity because a doesn't know it.
        # So we swap as needed and keep going until the end. 
        # The very last one is the only candidate. We then need to make sure that everyone knows it
        # and that its indegree == n-1
        
        ptr = 0
        while ptr < n - 1:
            # If false
            if not knows(candidate[ptr], candidate[ptr+1]):
                # Swap a/b
                candidate[ptr], candidate[ptr + 1] = candidate[ptr + 1], candidate[ptr]
                
            # Increment
            ptr += 1
        # print(candidate)
            
        if is_celebrity(n, candidate[-1]):
            return candidate[-1]
        else:
            return -1