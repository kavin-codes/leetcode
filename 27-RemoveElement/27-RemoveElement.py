nums=[0,1,2,2,3,0,4,2]
val = 2


class Solution:
    def single(self,nums,val):
        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

s1=Solution()
print(s1.single(nums,val))