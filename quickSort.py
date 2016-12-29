class QuickSort():
  def partition(self, array, start, end): 
    if (start > end): return None 
    elif (start == end): return start 
    else:
      pivot = array[end]
      p = start-1 
      for i in range(start, end):
        if (array[i] <= pivot): 
          p += 1 
          array[p], array[i] = array[i], array[p]
          
      p += 1 
      array[p], array[end] = array[end], array[p]
      return p 
    
  def QSort(self,array,start,end): 
    
    if (start >= end): return array 
    pivot = self.partition(array, start, end)
    self.partition(array, start, pivot-1)
    self.partition(array, pivot+1, end)
    
    return array 
## For testing purpose 
"""
a = QuickSort()
b = a.QSort([3,5,10,4,8,11,7],2,3)
print(b)
"""
