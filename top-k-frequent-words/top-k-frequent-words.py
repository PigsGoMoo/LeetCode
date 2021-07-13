import heapq, collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.defaultdict(int)
        
        for word in words:
            counter[word] += 1
            
        max_heap = []
        
        for word in counter:
            heapq.heappush(max_heap, (-counter[word], word))
            
        ans = []
        
        for i in range(k):
            ans.append(heapq.heappop(max_heap)[1])
            
        return ans
        