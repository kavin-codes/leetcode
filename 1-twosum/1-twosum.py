nums=[2,7,11,15]
target=9

class solution:
    def single(self , nums):
        d={}
        for i in range(len(nums)):

            need =target-nums[i]

            

            if need in d:
                return [d[need],i]

            d[nums[i]]=i
    
s1=solution()
print(s1.single(nums))




        
