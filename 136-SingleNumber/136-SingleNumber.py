class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
    
nums = [2,2,1]
S1=Solution()
print(S1.singleNumber(nums))