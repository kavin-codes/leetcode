nums1 = [1,2,2,1] 
nums2 = [2,2]




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
                count=min(freq1[answer],freq2[answer])
                res.extend([answer]*count)
                
        
        return res

s1=solution()
print(s1.single(nums1,nums2))


