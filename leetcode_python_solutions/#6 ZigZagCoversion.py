class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        rows  = [""] *numRows
        curRow  = 0
        goDown = False
        for i in range(0,len(s)) :
            rows[curRow] = rows[curRow] + s[i]
            if (curRow  == 0 or curRow == numRows -1) :
                goDown = not goDown
            
            curRow += 1 if goDown else -1
        
        return "".join(rows)