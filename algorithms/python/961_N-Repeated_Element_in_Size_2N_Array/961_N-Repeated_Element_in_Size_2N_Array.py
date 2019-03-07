class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(0,len(A)-1):
            if A[i] in A[i+1:]:
                return A[i]
                
            