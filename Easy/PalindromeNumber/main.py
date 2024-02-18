class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
    
        num = n
        reversed_num = 0

        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10

        return n == reversed_num