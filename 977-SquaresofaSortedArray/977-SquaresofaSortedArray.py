nums = [-7, -3, 2, 3, 11]

class Solution:
    def single(self, nums):
        left = 0
        right = len(nums) - 1
        pos = len(nums) - 1
        res = [0] * len(nums)

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                res[pos] = left_sq
                left += 1
            else:
                res[pos] = right_sq
                right -= 1

            pos -= 1

        return res

s1 = Solution()
print(s1.single(nums))
