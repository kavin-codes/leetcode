class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()        # remove spaces at the end
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            count += 1

        return count


s = "Hello World"
obj = Solution()
print(obj.lengthOfLastWord(s))