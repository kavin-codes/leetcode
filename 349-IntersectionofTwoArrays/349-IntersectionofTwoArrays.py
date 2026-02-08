nums1 = [4,9,5,6,4,9] 
nums2 = [4,9]




class solution:
    def single(self,nums1,nums2):


        freq1={}
        freq2={}

        for num in nums1:

            if num in freq1:
                freq1[num]+=1
            else:
                freq1[num]=1

            

        for num in nums2:
            if num in freq2:
                freq2[num]+=1
            else:
                freq2[num]=1
        
            
        res=[]

        for answer in freq1:
            if answer in freq2:
                res.append(answer)
        
        return res

s1=solution()
print(s1.single(nums1,nums2))


