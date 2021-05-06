class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ans = []

        for interval in intervals:
            # Check for overlap
            # Overlap would mean that the first value of this current interval is less than the last value
            # of the last index in ans (because it's sorted)
            # If not overlap, that means new interval to append to ans
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                # Otherwise, merge it.
                ans[-1][1] = max(ans[-1][1], interval[1])
                
        return ans
        