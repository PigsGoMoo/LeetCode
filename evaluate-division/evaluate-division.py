class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def iterate_graph(accum, curr, target, visited):
            visited.add(curr)
            res = -1.0
            neighbors = graph[curr]
            
            if target in neighbors:
                res = accum * neighbors[target]
            
            else:
                for neighbor, weight in neighbors.items():
                    if neighbor not in visited:
                        res = iterate_graph(accum * weight, neighbor, target, visited)
                        if res != -1.0:
                            break
                            
            visited.remove(curr)
            return res
            
        
        # Make our graph
        graph = collections.defaultdict(collections.defaultdict)
        
        # We need a weighted and directed graph. The opposite way can just be figured out
        # by inversing the value
        for (dividend, divisor), result in zip(equations, values):
            graph[dividend][divisor] = result
            graph[divisor][dividend] = 1/result
            
        # Initialize answer array
        ans = []
        # Loop through queries and solve
        for dividend, divisor in queries:
            # If same, return 1
            # Error for the question. Should be 1 but they want -1
            if dividend == divisor:
                res = 1.0
                if dividend not in graph:
                    res = -1.0
            # If one doesn't appear in the graph, we can't solve
            elif dividend not in graph or divisor not in graph:
                res = -1.0
            # Otherwise, solve based on our graph
            else:
                visited = set()
                
                res = iterate_graph(1, dividend, divisor, visited)
                
            ans.append(res)
            
        
        return ans