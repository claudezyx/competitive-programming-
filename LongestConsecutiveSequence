class Solution(): 
  def longestIncreasingSequence(self, array):
    length = len(array)
    if (length == 1): return array
    start = end = 0
    previous = next = 0
    largest = 1
    count = 1
    for i in range(1,length):
      if (array[i] == array[next] + 1):
        count += 1 
        next += 1
      else: 
        if (count > largest):
          start, end = previous, next 
          largest = count 
        previous = next = i 
        count = 1 
        
    if (count > largest):
      largest = count 
      start, end = previous, next 
      
    return array[start:end+1] 
    
## For testing purpose
"""
a = Solution()
b = [1,2,3,1,2,3,4,5,6] 
#b = [8,-1,6,7,2,18,-12]
print(a.longestIncreasingSequence(b))
"""
      
