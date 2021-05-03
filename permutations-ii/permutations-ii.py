class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Solution to permutation I. Works, but slow.
        ans = []
        length = len(nums)
        
        
#         def backtracker(start):
#             # print("Backtracker called with starting index of {} and current nums formation of {}".format(start, nums))
#             if start == length:
#                 if nums not in ans:        
#                     # print("Appending unique combination of nums to answer: {}".format(nums))
#                     ans.append(nums[:])
#                     # print("Current answers: {}".format(ans))
#                 return
                
            
#             for i in range(start, length):
#                 nums[start], nums[i] = nums[i], nums[start]
#                 # print("Swapped start index {} with current index {}. Calling backtracker".format(start, i))
                
#                 backtracker(start + 1)
                
#                 nums[start], nums[i] = nums[i], nums[start]
#                 # print("Reverse swapping of indexes {} and {}: {}".format(start, i, nums))
                
                
#         backtracker(0)
#         return ans
        
        # In order to improve this answer, we can use a hash table to keep a counter of the unique numbers
        # Using ans and length variables defined above
        
        def backtracker(path, counter):
            
            if len(path) == length:
                ans.append(path[:])
                return
            
            
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    
                    backtracker(path, counter)
                    
                    path.pop()
                    counter[num] += 1
                    
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        backtracker([], counter)
        
        return ans
            