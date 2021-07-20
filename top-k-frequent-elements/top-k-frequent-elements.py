import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a heap. Heaps are O(n log k)
        # Better is quick select - O(n)
        
        # Heap version
        max_heap = []
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for key in counter:
            heapq.heappush(max_heap, (-counter[key], key))
            
        ans = []
        
        for _ in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        
        return ans
        
        