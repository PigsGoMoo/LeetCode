# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ptr = 0
        print(len(nestedList))
        self.arr = self.flatten(nestedList)
        
    def flatten(self, arr):
        ans = []
        for i in range(len(arr)):
            if arr[i].isInteger():
                ans.append(arr[i].getInteger())
            else:
                flat = self.flatten(arr[i].getList())
                for item in flat:
                    ans.append(item)
                
        return ans
    
    
    def next(self) -> int:
        res = self.arr[self.ptr]
        self.ptr += 1
        return res
    
    def hasNext(self) -> bool:
        return self.ptr < len(self.arr)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())