class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Use min heap to grab all items
        # Slowly pop out one by one. If it's viable, keep going. If not, return False
        
        # Edge case - if not divisible by groupSize, we can't make it
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        
        for card in hand:
            count[card] = count.get(card, 0) + 1
        
        
        i = 0
        while i < len(hand):
            
            # print("Current count: {}".format(count))
            if i % groupSize == 0:
                last_item = min(count.keys())
                # print("Grabbed lowest item: {}".format(last_item))
                count[last_item] -= 1
                if count[last_item] == 0:
                    del count[last_item]
                
            else:
                current_item = last_item + 1
                # print("Checking for current item: {}".format(current_item))
                
                if current_item not in count:
                    return False
                
                count[current_item] -= 1
                if count[current_item] == 0:
                    del count[current_item]                
                
                last_item = current_item
                
            i += 1
            
            
        return True
            