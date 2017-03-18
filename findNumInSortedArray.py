def binarySearch(array,num):
  """
  Find the target: num in an sorted array with duplicates 
  """
  count = 0 
  length = len(array)
  start, end = 0, length-1
  while(end >= start): 
    mid = int((end+start)/2)
    if array[mid] < num:
      start = mid + 1 
    elif array[mid] > num:
      end = mid - 1 
    else: 
      count += 1 
      i = mid - 1 
      while (i >=0 and array[i] == num):
        count += 1 
        i -= 1 
      i = mid + 1 
      while (i <= length-1 and array[i] == num): 
        count += 1 
        i += 1 
      break 
  
  return count 
      
