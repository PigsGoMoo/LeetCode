class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Easiest to probably do DFS
        # Start at node
        # Iterate through neighbors, recursively calling DFS
        # Graph is acyclic, so no need to keep track of visited
        # If hit final node, add path to ans array
        
        ans = []
        
        def dfs(node, path):
            # Base case
            if node == len(graph) - 1:
                ans.append(path)
                return
            
            # Iterate through each neighbor
            for nei in graph[node]:
                dfs(nei, path + [nei])
                
        
        dfs(0, [0])
        return ans
            