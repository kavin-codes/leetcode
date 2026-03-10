class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_len = 0
        seen = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in seen:
                max_len = max(max_len, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        return max_len


nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
sol = Solution()
print(sol.findMaxLength(nums))