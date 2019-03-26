class Solution:
    def sortedMerge(A, B):
        i_A = len(A) - len(B)
        i_B = len(B)
        i = len(n) - 1
        while(i_B >= 0):
            if(i_A < 0 or A[i_A] < B[i_B]):
                A[i] = B[i_B]
                i -= 1
                i_B -= 1
            elif(A[i_A] == B[i_B]):
                A[i] = A[i_A]
                i -= 1
                i_A -= 1
                A[i] = B[i_B]
                i -= 1
                i_B -= 1
            else:
                A[i] = A[i_A]
                i -= 1
                i_A -= 1
