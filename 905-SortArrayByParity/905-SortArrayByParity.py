nums = [3, 1, 2, 4, 5, 6]

class Solution:
    def single(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums        

s1 = Solution()
print(s1.single(nums))
