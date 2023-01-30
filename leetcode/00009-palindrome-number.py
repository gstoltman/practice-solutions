class Solution:
    def isPalindrome(self, x: int) -> bool:
        xinput = x
        rev = 0
        while x > 0:
            remainder = x % 10
            rev = (rev * 10) + remainder
            x = x // 10
        if xinput == rev:
            return True
        else:
            return False
