class Solution: 
    def countOccurence(self, array):
	"""Given an unsorted array of n integers which can contain integers from 1 to n. 
	Some elements can be repeated multiple times and some other elements can be absent from the array. 
	Count frequency of all elements that are present and print the missing elements."""
        length = len(array)
        i = 0 
        while (i < length):
            if (array[i] <0):
                i += 1 
            else: 
                elementIndex = array[i] - 1
                if (array[elementIndex] > 0): 
                    array[i] = array[elementIndex]
                    array[elementIndex] = -1 
                else: 
                    array[elementIndex] -= 1 
                    array[i] = 0 
                    i += 1 
        print(array)
        
        return array 
a = Solution()
a.countOccurence([2, 3, 3, 2, 5])
a.countOccurence([1])
a.countOccurence([4, 4, 4, 4])
a.countOccurence([1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1])
a.countOccurence([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
a.countOccurence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
a.countOccurence([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
