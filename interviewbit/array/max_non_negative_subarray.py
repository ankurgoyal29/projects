class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        h = {}
        temp_sum = 0
        temp_count  = 0
        temp_index = -1
        
        def check():
            if temp_sum in h:
                if temp_count > h[temp_sum][1]:
                    h[temp_sum] = [temp_index, temp_count]
            else:
                h[temp_sum] = [temp_index, temp_count]
                
        for i, v in enumerate(A):
            if v >=0:
                if temp_index < 0:
                    temp_index = i
                temp_count +=1
                temp_sum += v
            else:
                if temp_count > 0 : check()
                temp_count = 0
                temp_sum = 0
                temp_index =-1
        
        if temp_count > 0 :check()
            
        final = []
        if len(h.keys()) == 0 :
            return []
        for i in range(h[max(h.keys())][0], len(A)):
            if A[i] >=0:
                final.append(A[i])
            else:
                return final
        return final
