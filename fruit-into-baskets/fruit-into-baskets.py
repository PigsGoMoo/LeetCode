class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxCount = 0
        
        tracker = {}
        
        left = right = 0
        
        tracker[tree[0]] = 1
        
        while right < len(tree):
            # Increment right until it hits a new number
            while len(tracker) <= 2 and right + 1 < len(tree):
                right += 1
                tracker[tree[right]] = tracker.get(tree[right], 0) + 1
            
            # Update max count
            # We don't add +1 here because the +1 includes the next number. If we're at the end, right will
            # still have one too many points
            if len(tracker) > 2:
                maxCount = max(maxCount, right - left)
                # print("Updating maxCount to {}".format(maxCount))
            
            # If we've reached end, update maxCount and break
            if right == len(tree) - 1:
                if len(tracker) <= 2:
                    maxCount = max(maxCount, right - left + 1)
                # print("Updating maxCount to {}".format(maxCount))
                break
            # print("Right index: {}".format(right))
            # Otherwise, remove the left value from tracker
            remove = tree[left]
            
            # Increment left until we're at a different number
            while tree[left] == remove and left <= right and len(tracker) > 2:
                # Decrement the item at left tracker
                # print("Removing {} from tracker {}".format(remove, tracker))
                if tracker[tree[left]] >= 2:
                    tracker[tree[left]] -= 1
                else:
                    tracker.pop(tree[left])
                left += 1
            # print("Left index: {}".format(left))
        # print("Returning {}".format(maxCount))    
        return maxCount