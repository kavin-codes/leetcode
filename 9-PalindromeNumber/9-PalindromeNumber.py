class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10


obj = Solution()

print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))