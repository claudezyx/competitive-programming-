class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        length = len(A) 
        A.sort() 
        storage = [[[0 for t in range(target+1)] for j in range(k+1)] for i in range(length+1)] 
        for i in range(length+1):
            storage[i][0][0] = 1
            
        for i in range(1,length+1):
            j = 1
            while (j <= i and j <= k):
                for t in range(1,target+1): 
                    storage[i][j][t] = storage[i-1][j][t]
                    if ((t - A[i-1]) >= 0): 
                        storage[i][j][t] += storage[i-1][j-1][t-A[i-1]]
                j += 1 
        return storage[length][k][target] 
        
