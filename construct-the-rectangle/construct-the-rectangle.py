class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        closest = int(area ** (1/2))
        
        while area % closest != 0:
            closest -= 1
            
        return [area // closest, closest]
        