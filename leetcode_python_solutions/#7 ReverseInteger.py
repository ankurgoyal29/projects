class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        ans = int(s[::-1]) if x > 0 else - int(s[::-1])
        return ans if ans >= -1<<31 and ans <= (1 <<31 )-1 else 0
        