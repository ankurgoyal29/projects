class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0) ) :
            return False
        
        newNumber  = 0
        while x > newNumber :
            rem = x%10
            newNumber  = newNumber * 10 + rem
            x = x//10
        
        return  newNumber == x or x == newNumber//10

    
#Intution 

# Second idea would be reverting the number itself, and then compare the number with original number, if they are the same, then the number is a palindrome. However, if the reversed number is larger than int.MAX\text{int.MAX}int.MAX, we will hit integer overflow problem.

# Following the thoughts based on the second idea, to avoid the overflow issue of the reverted number, what if we only revert half of the int\text{int}int number? After all, the reverse of the last half of the palindrome should be the same as the first half of the number, if the number is a palindrome.

# For example, if the input is 1221, if we can revert the last part of the number "1221" from "21" to "12", and compare it with the first half of the number "12", since 12 is the same as 12, we know that the number is a palindrome.

# Let's see how we could translate this idea into an algorithm.