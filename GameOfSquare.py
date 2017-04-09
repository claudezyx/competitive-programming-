'''
Game of squares
Two players
Turn: Subtracting a perfect square from the current state
State: Always a non-negative integer
50
41
37
...
1,4,9,16
1 1 
2 0 :negative
3,1 
4,4
5,1 : negative 
6 -5 = 1 
6
5 -1 4
5-4 1 
6: 1,1,4
2: 1,1

8: 4+4 1
7: 1, 4
6, 3
2
1
0
An An+1


i = 4
negativeIndex = 2
array: 1,-1, 1
move = findSquare(4, [1, -1, 1, 0])
'''
(n*squr(n))
def getOptimalMove(currentState):
    array = [-1 for i in range(currentState+1)]
    for i in range(1, currentState+1):
        for j in range(1, int(sqrt(i)) + 1):
            if (array[i - j*j] = -1):
                array[i] == j*j
                
    return array[currentState]


def getOptimalMove(currentState):
    
    array = [0 for i in range(currentState)]
    array[0] = 1
    negativeIndex = None 
    for i in range(2,currentState+1): 
        if not negativeIndex: 
            negativeIndex = i
            array[i-1] = -1
        else: 
            move = findSquare(currentState, array) 
            array[i-1] = move 
    return array[-1]
    
def findSquare(currentState,array):
    i = 1 
    while (i**2 <= currentState): 
        if array[currentState - i**2 - 1] < 0:#4-4-1 = 2 
            return i**2
        i += 1 
        
