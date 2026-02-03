s = "loveleetcode"

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        
        for i, ch in enumerate(s):
            if d[ch] == 1:
                return i

        return -1
    
s1=Solution()
print(s1.firstUniqChar(s))
    
