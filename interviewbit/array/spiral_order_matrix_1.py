class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        t, b, l, r = 0, len(A)-1, 0, len(A[0])-1
        dir = 0
        res = []
        while (t <= b and l <= r):
            if dir == 0:
                for i in range(t, r+1):
                    res.append(A[t][i])
                dir = 1
                t +=1
            elif dir == 1:
                for i in range(t, b+1):
                    res.append(A[i][r])
                dir =2 
                r -=1
            elif dir == 2:
                for i in range(r, l-1, -1):
                    res.append(A[b][i])
                dir =3
                b -=1
            else:
                for i in range(b, t-1, -1):
                    res.append(A[i][l])
                dir = 0 
                l +=1
        return res
