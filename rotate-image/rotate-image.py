class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        # Only need to iterate through half because the rotation will take care of the rest.
        # First loop determines how many iterations
        for i in range(n//2 + n%2):
            # Second loop determines how many times per iteration
            for j in range(n//2):
                # Each time, we'll swap the 4 values at a time
                
                # Store bottom left number in temp
                temp = matrix[n - 1 - j][i]
                # Replace bottom left number with bottom right
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                # Replace bottom right number with top right
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                # Replace top right number with top left
                matrix[j][n - 1 - i] = matrix[i][j]
                # Replace top left with value stored in temp
                matrix[i][j] = temp                