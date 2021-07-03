import heapq

class Solution:
    
    # Used in DFS approach
    def __init__(self):
            self.adj_matrix = None
            self.memo = {}
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 4 methods to solve this
        # Can use Dijkstra's algo
        # Can use a regular DFS
        # Can use Bellman Ford
        # Can use BFS
        
#         # Dijkstra's uses a min heap and adjacency matrix in order to traverse the graph
#         # Doesn't work for one specific test case. Premium solution lied.
#         # All nodes other than starting node start out with a distance of inf
#         # It relaxes the next node in the min heap each time until heap runs out
#         # We need to modify it so that it will reconsider a worse path in case the better(shorter) path
#         # goes over the step limit
        
#         # First, build adjacency matrix
#         adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        
#         for start, dest, cost in flights:
#             adj_matrix[start][dest] = cost
            
#         for i in range(len(adj_matrix)):
#             print(i, adj_matrix[i])
            
#         print("We want to go from {} to {}".format(src, dst))
#         # Make array to keep track of shortest distances
#         distances = [float('inf') for _ in range(n)]
#         current_stops = [float('inf') for _ in range(n)]
#         distances[src], current_stops[src] = 0, 0
        
#         # Initialize our min heap. Each item in heap will be a tuple of (cost, stops, node)
#         min_heap = [(0, 0, src)]
        
#         # Go until min_heap is empty
#         while min_heap:
#             cost, stops, node = heapq.heappop(min_heap)
#             print("Current node: {}, cost to get here: {}, stops made: {}".format(node, cost, stops))
            
#             # Base cases:
#             # If destination reached:
#             # if node == dst:
#             #     return cost
            
#             # Too many steps taken
#             # We need to do K + 1 because that's the number of edges allowed given number of stops K
#             if stops == k + 1:
#                 continue
                
#             # For each item in heap, we need to examine and relax the neighboring edges
#             # So iterate through every node
#             for neighbor in range(n):
#                 # If the neighbor is adjacent to our current node
#                 if adj_matrix[node][neighbor] > 0:
#                     # Grab the values of the nodes and cost
#                     # Current cost to get to node U from start
#                     dU = cost
#                     # current cost to go to node V from start point
#                     dV = distances[neighbor]
#                     # Cost to go from node U to node V
#                     wUV = adj_matrix[node][neighbor]
#                     print("Next node: {}, current distance to node: {}, distance from current node to that node: {}"
#                           .format(neighbor, dV, wUV))
                    
#                     # If can be relaxed - aka cost to get to node U plus cost to go from U -> V is less than
#                     # the current cost to go from start to V
#                     if dU + wUV < dV:
#                         # Then we relax it
#                         print("Shorter path found through this node")
#                         distances[neighbor] = dU + wUV
#                         # Push this new value back into the heap so we can reevaluate anything it leads to
#                         heapq.heappush(min_heap, (dU + wUV, stops + 1, neighbor))
                        
#                     # Otherwise, if we're still below the max number of stops
#                     if stops < current_stops[neighbor]:
#                         # Add it again so we can reconsider if the shorter path doesn't make it within the amount of stops
#                         current_stops[neighbor] = stops
#                         print("Less stops to get to this node")
#                         heapq.heappush(min_heap, (dU + wUV, stops + 1, neighbor))
                        
#         # If our distances array for dst node hasn't been updated (aka still inf), then that means we
#         # can't reach the destination in the given amount of steps. So we return -1
#         # If it isn't inf, then we've reached it and that's the cheapest possible route. 
#         return -1 if distances[dst] == float('inf') else distances[dst]
                    
        # DFS solution:
        
        # Make our adjacency matrix
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
            
        result = self.find_shortest(src, k, dst, n)
        return -1 if result == float('inf') else result
    
    def find_shortest(self, node, stops, dst, n):
        # Base case
        # If we're at destination
        if node == dst:
            return 0
        
        # If we're out of moves
        if stops < 0:
            return float('inf')
        
        # If in cache
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recursively call itself for each neighbor
        ans = float('inf')
        for neighbor in range(n):
            # If it's a neighbor
            if self.adj_matrix[node][neighbor] > 0:
                # Recursively call to find the less costly path
                ans = min(ans, self.find_shortest(neighbor, stops-1, dst, n) + self.adj_matrix[node][neighbor])
                
        # Cache result
        self.memo[(node, stops)] = ans
        return ans
                