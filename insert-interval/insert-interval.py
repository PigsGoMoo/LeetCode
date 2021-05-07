class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Destructure
        new_start, new_end = newInterval
        
        # Initialize
        idx = 0
        n = len(intervals)
        ans = []
        
        # Add intervals that start before the new one does
        while idx < n and new_start > intervals[idx][0]:
            ans.append(intervals[idx])
            idx += 1
            
        # Now add in the new interval where it belongs
        
        # First check overlap
        if not ans or ans[-1][1] < new_start:
            ans.append(newInterval)
            
        else:
            # IF there is overlap, merge it
            ans[-1][1] = max(ans[-1][1], new_end)
            
        # Add rest of the intervals, merging if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            
            # If no overlap, just add interval
            if ans[-1][1] < start:
                ans.append(interval)
            # Otherwise, merge
            else:
                ans[-1][1] = max(ans[-1][1], end)
                
        return ans
            
                
            