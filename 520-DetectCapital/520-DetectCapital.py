class Solution:
    def detectCapitalUse(self, word):
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False

word = input("Enter word: ")
obj = Solution()
result = obj.detectCapitalUse(word)
print(result)