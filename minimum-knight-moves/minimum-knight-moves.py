from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
#         # Use something similar to dijkstra's
        
#         # Make our list of possible moves
#         moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
#         # Helper func to traverse in dijkstra fashion
#         def traverse(x, y):
            
#             # Initialize a visited and queueue for bfs
#             visited = set()
#             q = collections.deque([(0,0)])
#             ans = 0
            
#             while q:
#                 count = len(q)
#                 # Iterate through the first set of possible moves for every item on this level
#                 for i in range(count):
#                     curr_x, curr_y = q.popleft()
#                     # Mark as visited
#                     visited.add((curr_x, curr_y))
#                     # If this is our destination, return
#                     if curr_x == x and curr_y == y:
#                         return ans
                    
#                     # Otherwise, add each possible movement to the queueueue
#                     for dx, dy in moves:
#                         new_x, new_y = curr_x + dx, curr_y + dy
                        
#                         # If we haven't been here yet, add to queueueueue
#                         if (new_x, new_y) not in visited:
#                             q.append((new_x, new_y))
#                 # At the end of each set of possible moves, increment ans
#                 ans += 1
#                 # We should be at the end before exiting the while loop because it's guaranteed to be reachable
            
            
#         return traverse(x, y)
        # Taking this one step further,
        # Since everything is symmetrical, we can actually just find the value in one of the quadrants
        # Because the value to get to that one area in that one quadrant is the same as if it were
        # in the same place in any of the other quadrants
        
        # Keeping this in mind, we can have our piece move right and up until we hit the target in the first quadrant
        # Since we're going straight for it, this is a DFS approach
        # Our base case will be when we hit our target or when we hit a spot known as the immediate neighborhood
        # From this spot, we would need to make exactly two moves (in a zigzag pattern) to get to the final
        # and thus, if we're only checking the up-right movements, we won't be able to find it
        # So we need to make this one of our base cases
        # Actually, instead of going to the target, it would be easier to make the func if we go from target to 0
        
        # Use memoization to prevent recalculation
        @lru_cache(maxsize=None)
        def dfs(x, y):
            
            # Base cases
            # If target reached
            if (x, y) == (0, 0):
                return 0
            
            # Immediate neighborhood for 0 are at points (1, 1), (0, 2), and (2, 0) in quadrant 1
            elif x + y == 2:
                # Takes two steps to get to 0 from here
                return 2
            
            else:
                # Otherwise, call dfs recursively for our two possible moves
                # Since we're going from target to 0 now, instead of up-right, we go down-left
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
            
            
        return dfs(abs(x), abs(y))
