"""
Given a list of integers, return the number that appears second most frequently.
For example, [0,1,2,2,2,2,1,0,5,1] would return 1 
Python Collection Module 
https://pymotw.com/2/collections/counter.html
"""
import collections 
class Solution(): 
  def findSecondMostFrequent(self, array):
    c = collections.Counter()
    c.update(array)
    return c.most_common(2)[1][0]

###For testing purpose
"""
a = Solution()
b = [0,1,2,2,2,2,1,0,5,1]
print(a.findSecondMostFrequent(b))
"""
