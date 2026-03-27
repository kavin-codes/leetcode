class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans


obj = Solution()


print(obj.mySqrt(4))  
print(obj.mySqrt(8))   
print(obj.mySqrt(15))  