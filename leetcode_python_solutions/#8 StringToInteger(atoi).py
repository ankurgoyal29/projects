class Solution:
    def myAtoi(self, s: str) -> int:
        newStr = ''
        isNeg = False
        checkSign = False
        s = s.lstrip(' ')
        for char in s :
            if char == ' ' and checkSign ==False :
                continue
            if char == '-' and checkSign == False :
                isNeg= True 
                checkSign = True
                continue
            if char == '+' and checkSign == False :
                checkSign  = True
                continue
            
            if char.isnumeric() :
                newStr += char
                checkSign = True
            else:
                break

        if newStr  == '' :
            return 0
        ans = int(newStr) if not isNeg else - int(newStr)
    
        IntMin = -1<<31
        IntMax= (1 <<31) -1
        if (ans < IntMin) :
            return  IntMin
        elif ans >= IntMax :
            return IntMax
