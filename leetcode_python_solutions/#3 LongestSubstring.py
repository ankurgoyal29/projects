class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strlen =  len(s)
        if (strlen == 0) :
            return 0
        hashindex = {}
        ans = 0
        temp  = 0
        for i in range(0, strlen) :
            if(s[i] in hashindex) :
                diff = i - hashindex[s[i]]
                if  diff <= temp :
                    ans  = max(ans, temp)
                    temp = diff
                else :
                    temp = temp+1
            else :
                temp += 1
            
            hashindex[s[i]] = i
        return max(temp, ans)