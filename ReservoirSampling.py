"""
https://en.wikipedia.org/wiki/Reservoir_sampling
"""

"""
Return only one index of the max number with equal chance 
[1, 2, 3, 2, 3]
In this case, the function should return 2 or 4 with equal chance 
"""
import sys
import random 
def produceMaxNumIndex(numArray):  
    maxIndex = -1
    maxNum = -sys.maxsize()
    lenght = len(numArray)
    for i in range(length): 
        if numArray[i] > maxNum: 
            maxIndex = i
            count = 1   
        
        if numArray[i] == maxNum:
            count += 1 
            maxIndex = seselectBetweenTwoIndices(maxIndex,i,count)
    return maxIndex 

            
def selectBetweenTwoIndices(maxIndex,currentIndex,count):
    # Integer from 1 to count inclusive
    randomNumber = random.randrange(1,count+1)
    if randomNumber < count: 
        return maxIndex
    else: 
        return currentIndex
    
            
