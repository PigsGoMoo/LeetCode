class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use something similar to Dijkstra
        # BFS your way up
        
        q = collections.deque([(amount, 0)])
        seen = set()
        
        while q:
            remain, steps = q.popleft()
            
            if remain == 0:
                return steps
            
            for coin in coins:
                if remain - coin >= 0 and remain - coin not in seen:
                    q.append((remain - coin, steps + 1))
                    seen.add(remain - coin)
                    
        return -1
                    