class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        minIndex = A[0]
        c = []

        for i in range(len(A)):
            if ( A[i] <= A[minIndex]):
                c.append(-1)
                minIndex = i
            else:
                for j in range(i, minIndex-1, -1):
                    if (A[j] < A[i]):
                        c.append(A[j])
                        break
            
        return c                