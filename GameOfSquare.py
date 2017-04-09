"""
Game of squares
Two players
Turn: Subtracting a perfect square from the current state,excluding 0 
State: Always a non-negative integer
"""
import math 

def getOptimalMove(currentState):
    array = [-1 for i in range(currentState+1)]
    for i in range(1, currentState+1):
        upperBound = int(math.sqrt(i)) + 1
        for j in range(1, upperBound):
            if (array[i - j*j] = -1):
                array[i] == j*j             
    return array[currentState]



