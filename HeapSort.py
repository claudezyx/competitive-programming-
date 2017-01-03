class Solution(): 
  def Heapify(self, array, parentIndex): 
    leftChildIndex = parentIndex * 2 + 1 
    rightChildIndex = parentIndex * 2 + 2 
    largestI = parentIndex
    if (leftChildIndex < len(array) and array[leftChildIndex] > array[largestI]):
      largestI = leftChildIndex
    if (rightChildIndex < len(array) and array[rightChildIndex] > array[largestI]):
      largestI = rightChildIndex
    if (largestI != parentIndex):
      array[parentIndex], array[largestI] = array[largestI], array[parentIndex] 
      self.Heapify(array, largestI)
    return 
    
  def ConstructHeap(self, array): 
    length = len(array)
    if (length == 1): return array
    start = int(length/2) - 1
    end = -1 
    for i in range(start, end, -1):
      self.Heapify(array, i)
    return array 
  
  def HeapSort(self, array): 
    length = len(array) 
    if (length == 1): return array
    array = self.ConstructHeap(array)
    last = length - 1
    while (last > 0):
      array[0], array[last] = array[last], array[0]
      array[:last] = self.ConstructHeap(array[:last]) 
      last -= 1 
    return array
## For testing purpose
""" 
a = Solution()
b = [4,2,3,0,10]
print(a.HeapSort(b))
"""
