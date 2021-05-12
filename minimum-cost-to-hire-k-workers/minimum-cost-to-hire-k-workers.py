class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # We solve this by making the ratios of wage to quality and sort that in ascending order
        # Because we won't be able to decrease the ratio of anyone's wages - we can only increase it
        # So then smaller ratios will become irrelevant
        # Then we make a min heap based on quality. Lower qualities make for cheaper wages.
        # We multiply that with the current ratio to get our answer.
        # Python comes with a maxheap. To use min heap, we just use maxheap of negative values.
        
        # Make our array of workers - will have ratio, quality, and wage
        # We'll need the fraction library to make our ratios
        from fractions import Fraction
        import heapq
        workers = sorted([(Fraction(w, q), q, w) for q, w in zip(quality, wage)])
        
        # Initialize variables
        # ans will store our ans - needs to be smallest answer, so initialize to largest num
        ans = float('inf')
        # Selections will store our pool of workers. It'll be a maxheap of negative q values (aka a min heap)
        selections = []
        # sumq is the sum of the selections heap
        sumq = 0
        
        for ratio, q, w in workers:
            # Push -q value into heap
            heapq.heappush(selections, -q)
            # Increase sum by q value
            sumq += q
            
            # If we have too many values in the heap
            if len(selections) > k:
                # Get rid of the smallest
                remove = heappop(selections)
                # And subtract from sum (it'll be a negative value so we can just add here)
                sumq += remove
                
            # If we have the right amount of workers
            if len(selections) == k:
                # Calculate the cost
                # Cost will be the current sum times the current ratio
                # Because ratio is sorted in an increasing order, we can just use the current ratio.
                ans = min(ans, sumq * ratio)
                
        return float(ans)