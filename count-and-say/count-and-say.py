class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ["1"]
        
        for i in range(1, n + 1):
            count = 0
            next = ""
            for j in range(len(ans[i-1])):
                # print("In second for loop where j = {}, looking at {}".format(j, ans[i-1]))
                if j == 0:
                    # print("j = 0, so just incrementing count to 1")
                    count += 1
                elif ans[i-1][j] == ans[i-1][j-1]:
                    count += 1
                    # print("Current number {} same as previous number {}. Adding to count: {}".format(ans[i-1][j], ans[i-1][j-1], count))
                    
                else:
                    # print("Adding together {} + {} + {}".format(next, count, ans[i-1][j-1]))
                    next = next + str(count) + ans[i-1][j-1]
                    # print("Adding {} to tracker".format(next))
                    count = 1
            
            # print("Loop over. Adding {} and {} to next ('{}') before appending to ans".format(count, ans[i-1][j], next))
            next = next + str(count) + ans[i-1][j]
            ans.append(next)
            
        return ans[n-1]
        
        