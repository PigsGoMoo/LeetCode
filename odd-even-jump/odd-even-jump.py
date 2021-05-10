class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # First/odd jumps, number you're on has to be <= the number you jump to.
        # You have to choose the lowest of those possible values
        # Even jumps, number you're on has to be >= the number you jump to
        # You have to choose the greatest of those possible values
        # Aka: Odd - jump to smallest number >= than current. Even: Jump to largest number <= current
        
        # We can do this by mapping out the next possible jump. These jumps alternate between higher and lower
        # So we can make a map for each. If there's a higher jump at this index, we'll mark where it should be. 
        # And do the same with lower. Then we just alternate higher and lower until we hit a dead end or end.
        
        # Initialize variables
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        stack = []
        sortedA = []
        
        # Sort (a copy of) the list from lowest to highest
        for i, a in enumerate(arr):
            sortedA.append([a, i])

        sortedA.sort()

        # Then make the map. The map will be made using a stack. We'll traverse from lowest to highest
        # If the index of the next highest number comes after the current index, we'll add that to the map
        # Otherwise, we'll continue to make the stack bigger
        for a, i in sortedA:
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        # Then reset the stack and do it again with the lower values
        stack = []
        # Reverse the sorted list
        for arr in sortedA:
            arr[0] = -arr[0]

        sortedA.sort()
        # Make map of lower values
        for a, i in sortedA:
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        # Here we use the map for the next jump to determine whether or not we can get to the end
        # with a higher/lower jump.
        # Higher is gonna be if we can make it with a higher jump from this location
        # Lower is same with lower jump
        higher, lower = [0] * n, [0] * n
        # The very last value is set to true because we can get there if we're already there
        higher[-1] = lower[-1] = 1
        # So then from index last - 1, we check and see
        for i in range(n - 2, -1, -1):
            # If we can get there from higher because the next jump will be lower from the next highest
            # index. So if that jump comes up true, this will also be true
            higher[i] = lower[next_higher[i]]
            # Same here. If with the next lowest, we can get there with a higher jump, this will be set to true.
            lower[i] = higher[next_lower[i]]
        # Return the sum of the higher jumps because the first jump is always a higher jump
        return sum(higher)