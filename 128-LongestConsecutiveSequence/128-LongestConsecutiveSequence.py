
nums = [100,4,200,1,3,2]

class Solution():
    def single(self,nums):

        num_set=set(nums)
        longest=0


        for num in num_set:
            if num-1 not in num_set:
                current=num
                length=1

                while current+1 in num_set:
                    current+=1
                    length+=1


                longest=max(length, longest)

        return longest
        

s1=Solution()
print(s1.single(nums))





        