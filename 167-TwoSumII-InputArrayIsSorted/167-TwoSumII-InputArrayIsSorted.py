nums = [ 2, 3, 4, 11]
target = 9

class Solution:
    def single(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                return (left + 1, right + 1)
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return None  

s1 = Solution()
print(s1.single(nums, target))
