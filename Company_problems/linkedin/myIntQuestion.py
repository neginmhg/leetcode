
# Write an iterator that, given a (potentially nested) collection will iterate over the contents of the collections in order. Thus, given a collection containing ((1, 3, 5),(4, 7, 3),((2, 3), 4)) the deep iterator should return 1, 3, 5, 4, 7, 3, 2, 3, 4

#class Data:
#    def isInteger(self) -> bool:
#        """
#        @return True if this Data holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this Data holds, if it holds a single integer
#        Return None if this Data holds a nested list
#        """
#
#    def getList(self) -> [Data]:
#        """
#        @return the nested list that this Data holds, if it holds a nested list
#        Return None if this Data holds a single integer
#        """
#edge cases: nestedList can be empty
#time and space complexity 
from collections import deque

class DeepIteratorImpl:
    def __init__(self, nestedList: [Data]):
        self.result=deque()
        if (len(nestedList) !=0):
            self.result=self.transfromToList(nestedList)

    def transformToList(self, nestedList:[Data])-> list:
        q=deque(nestedList)
        result=deque()
        while q:
            element = q.popleft()
            if (element.isInteger()):
                result.append(element.getInteger())
            else:
                elementList= element.getList()
                for e in elementList:
                    q.append(e)
        return result

    def next(self) -> int:
        if(self.hasNext()):
            return self.result.popleft()
        else:
            return None
    
    def hasNext(self) -> bool:
        if(len(self.result)>0):
            return True
        return False

myList= [[1,2,3],4,[9]]
iter = DeepIteratorImpl(myList)
iter.next()