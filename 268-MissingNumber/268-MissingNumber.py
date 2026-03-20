class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


sol = Solution()
print(sol.missingNumber([3, 0, 1]))