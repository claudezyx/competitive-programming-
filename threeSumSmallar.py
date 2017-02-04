class Solution(): 
  def threeSumSmallar(self, array, target):
    length = len(array)
    if (length < 3): return 0 
    array.sort()
    total, i = 0, 0
    for i in range(length-2): 
      item = array[i] 
      twoSumTarget = target - item 
      total = total + self.find2SumClose(array[i+1:],twoSumTarget)
    return total 
  
  def find2SumClose(self, arr, target): 
    count = 0
    length = len(arr)
    if (length <2): return count
    arr.sort()
    pdex, qdex = 0, length-1
    while (pdex < qdex): 
      sum = arr[pdex] + arr[qdex]
      if (sum >= target): 
        qdex -= 1 
      else: 
        count += (qdex - pdex)
        pdex += 1 
    return count
    
"""     
a = Solution()
b = [-2, 0, 1, 3,5,7,9]
print(a.threeSumSmallar(b,10))
"""
