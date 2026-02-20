nums=[0,1,0,3,12]


class Solution:
    def single(self, nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1


s1=Solution()
s1.single(nums)
print(nums)


