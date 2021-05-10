class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        
        even = (l1 + l2) % 2 == 0
        
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        high = l1
        low = 0
        
        while low <= high: 
            
            x_partition = (high + low) // 2
            y_partition = ((l1 + l2 + 1) // 2) - x_partition
        
            x_left = nums1[x_partition - 1] if x_partition else float('-inf')
            x_right = nums1[x_partition] if x_partition != l1 else float('inf')
            
            y_left = nums2[y_partition - 1] if y_partition else float('-inf')
            y_right = nums2[y_partition] if y_partition != l2 else float('inf')
            
            if x_right >= y_left and y_right >= x_left:
                if even:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
                else:
                    return max(x_left, y_left)
                
            elif x_left > y_right:
                high = x_partition - 1
                
            else:
                low = x_partition + 1
        