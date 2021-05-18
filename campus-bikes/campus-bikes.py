class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # Make a list of all the distances, sorted, from lowest distance to highest, workers second, then bikes.
        
        distances = []
        
        for work_idx, worker in enumerate(workers):
            for bike_idx, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, work_idx, bike_idx))
                
        distances.sort()
        
        taken = set()
        ans = [-1] * len(workers)
        
        for distance, worker, bike in distances:
            # If bike hasn't been taken yet and worker hasn't been given a bike yet
            if bike not in taken and ans[worker] == -1:
                ans[worker] = bike
                taken.add(bike)
                
        return ans