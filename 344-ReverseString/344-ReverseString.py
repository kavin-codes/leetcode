s = ["h","e","l","l","o"]

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s1 = Solution()
s1.reverseString(s)
print(s)
