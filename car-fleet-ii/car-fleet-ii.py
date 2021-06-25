class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # 3x + 4 = 2x + 7
        # -2x = 2
        # ans = x2 - x1 / y1 - y2
        # Work from right to left
        # If speed of left value <= speed right val, then it can't catch up.
        # If calculation above yields a bigger value than the previous one, we ignore this calc
        # and calculate to the one before that (because collisions will happen and speed will be equal
        # to the one after since it can only collide if slower)
        # x = + 3
        
        # We can use a stack to keep track of the next values as well as ans array indexes
        stack = []
        n = len(cars)
        ans = [-1] * n
        
        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            # First get rid of anything that can't be calculated. Remember, the stack contains values to the right
            # because we're working right -> left, not left -> right
            while stack and (speed <= cars[stack[-1]][1] or \
                             (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1]) >= ans[stack[-1]] > 0):
                stack.pop()
                
            # After popping, we make calculation with next val in stack if stack because it's the valid one
            if stack:
                ans[i] = (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1])
            
            # Then we append current i value
            stack.append(i)
            
        return ans