class Solution:
    def containsDuplicate(self, nums):
        

        d={}

        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]==2:
                return True
            
 
        return False
    
nums=[1,2,3,1]
s1=Solution()
print(s1.containsDuplicate(nums))