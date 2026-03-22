class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        start = 0
        max_length = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            max_len = max(len1, len2)
            
            if max_len > max_length:
                start = i - (max_len - 1) // 2
                max_length = max_len
        
        return s[start:start + max_length]


obj = Solution()
print(obj.longestPalindrome("babad"))