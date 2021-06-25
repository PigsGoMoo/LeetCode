class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # Works but too slow
#         # Iterate through 2 values at a time
#         # If x2 - x1 <= k, we plug into formula y1 + y2 + abs(x1 - x2) + keep max
#         # Else, slide window
        
#         # Initialize window
#         left = 0
#         right = 1
#         ans = float('-inf')
        
#         while left < len(points) - 1:
#             # Check if difference less than k
#             # x value is 0th index
#             x_diff = abs(points[left][0] - points[right][0])
#             # print("Difference is: {}".format(x_diff))
            
#             if x_diff <= k:
                
#                 # Plug into formula and keep track of max
#                 ans = max(points[left][1] + points[right][1] + x_diff, ans)

#             # Iterate window
            
#             # We increase the right pointer if it's viable (diff <= k)
#             if right + 1 < len(points) and abs(points[left][0] - points[right + 1][0]) <= k:
#                 right += 1
#             # If not viable and left + 1 != right, we iterate left. Since x is strictly increasing, if this current
#             # left/right combo is viable, increasing left on x side will also be viable cuz diff will be smaller
#             elif left + 1 != right:
#                 left += 1
#                 right = left + 1
#             # Otherwise, we increment both sides of window
#             elif left + 1 == right:
#                 left += 1
#                 right += 1
        
#         return ans

        # New idea - same concept but we can use a queueue to keep track of the max in a given range
        # The formula y1 + y2 + |x1 - x2| can be simplified to y1 + y2 + x2 - x1 because x2 will always > x1
        # Further simplified to (y1 - x1) + (y2 + x2)
        # Our queue will have values [y - x, x] at every index
        queue = collections.deque()
        ans = float('-inf')
        
        for x, y in points:
            # While remove all values from queueuue that are outside of k range
            # Inside k range is x - queue[0][1] <= k
            while queue and x - queue[0][1] > k:
                queue.popleft()
            
            # If there are any items still in queue, that means it's within range
            # First one will be the highest value we can add
            if queue:
                ans = max(ans, x + y + queue[0][0])
                
            # Now remove all smaller y - x values from back because we want to only keep max values
            while queue and y - x >= queue[-1][0]:
                queue.pop()
                
            # Now we can append this to queue
            queue.append([y-x, x])
            
        return ans
            