nums = [1, 2, 3,1,1]
k = 3


class Solution:
    def single(self, nums, k):

        d={}
        

        for i , num  in enumerate(nums):

            if num in d:
                if i-d[num]<=k:
                    return True
            d[num]=i
        return False



    
s1=Solution()
print(s1.single(nums,k))